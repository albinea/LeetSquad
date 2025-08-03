from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from .models import Group, LeetCodeStats, ChatMessage
from .forms import CustomUserCreationForm, GroupCreationForm, JoinGroupForm
from .services import LeetCodeService

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    user_groups = request.user.joined_groups.all()
    created_groups = request.user.created_groups.all()

    from itertools import chain
    all_groups = list({g.id: g for g in chain(user_groups, created_groups)}.values())

    context = {
        'groups': all_groups,
        'user_groups': user_groups,
        'created_groups': created_groups,
    }
    return render(request, 'core/dashboard.html', context)

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.created_by = request.user
            group.save()
            group.members.add(request.user)
            messages.success(request, f'Group "{group.name}" created successfully!')
            return redirect('dashboard')
    else:
        form = GroupCreationForm()
    return render(request, 'core/create_group.html', {'form': form})

@login_required
def join_group(request):
    if request.method == 'POST':
        form = JoinGroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            try:
                group = Group.objects.get(name=group_name)
                if request.user not in group.members.all():
                    group.members.add(request.user)
                    messages.success(request, f'Successfully joined "{group.name}"!')
                else:
                    messages.info(request, f'You are already a member of "{group.name}".')
                return redirect('dashboard')
            except Group.DoesNotExist:
                messages.error(request, f'Group "{group_name}" does not exist.')
    else:
        form = JoinGroupForm()
    return render(request, 'core/join_group.html', {'form': form})

@login_required
def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    
    # Check if user is a member
    if request.user not in group.members.all() and request.user != group.created_by:
        messages.error(request, 'You are not a member of this group.')
        return redirect('dashboard')
    
    # Get group members with their stats
    members_stats = []
    for member in group.members.all():
        try:
            stats = member.leetcodestats
            members_stats.append({
                'user': member,
                'stats': stats,
                'total_solved': stats.total_solved,
            })
        except LeetCodeStats.DoesNotExist:
            members_stats.append({
                'user': member,
                'stats': None,
                'total_solved': 0,
            })
    
    # Sort by total problems solved (descending)
    members_stats.sort(key=lambda x: x['total_solved'], reverse=True)
    
    # Get recent chat messages (last 50, ordered by timestamp)
    messages_list = ChatMessage.objects.filter(group=group).order_by('timestamp')[:50]

    context = {
        'group': group,
        'members_stats': members_stats,
        'messages': messages_list,  # Remove the reversed() call
    }
    return render(request, 'core/group_detail.html', context)

@login_required
def update_stats(request):
    """Update current user's LeetCode stats"""
    try:
        user_stats = request.user.leetcodestats
        success = LeetCodeService.update_user_stats(user_stats)
        if success:
            messages.success(request, 'Stats updated successfully!')
        else:
            messages.error(request, 'Failed to update stats. Please check your LeetCode username.')
    except LeetCodeStats.DoesNotExist:
        messages.error(request, 'LeetCode stats not found. Please contact admin.')
    
    return redirect('dashboard')

@login_required
def get_group_members(request, group_id):
    """API endpoint to get group members and their stats"""
    group = get_object_or_404(Group, id=group_id)
    
    if request.user not in group.members.all() and request.user != group.created_by:
        return JsonResponse({'error': 'Access denied'}, status=403)
    
    members_data = []
    for member in group.members.all():
        try:
            stats = member.leetcodestats
            members_data.append({
                'username': member.username,
                'leetcode_username': stats.leetcode_username,
                'total_solved': stats.total_solved,
                'easy_solved': stats.easy_solved,
                'medium_solved': stats.medium_solved,
                'hard_solved': stats.hard_solved,
                'global_ranking': stats.global_ranking,
            })
        except LeetCodeStats.DoesNotExist:
            members_data.append({
                'username': member.username,
                'leetcode_username': 'N/A',
                'total_solved': 0,
                'easy_solved': 0,
                'medium_solved': 0,
                'hard_solved': 0,
                'global_ranking': None,
            })
    
    # Sort by total problems solved
    members_data.sort(key=lambda x: x['total_solved'], reverse=True)
    
    return JsonResponse({'members': members_data})
