from django.contrib import admin
from .models import Group, LeetCodeStats, ChatMessage

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'get_member_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    filter_horizontal = ['members']

@admin.register(LeetCodeStats)
class LeetCodeStatsAdmin(admin.ModelAdmin):
    list_display = ['user', 'leetcode_username', 'total_solved', 'global_ranking', 'last_updated']
    list_filter = ['last_updated']
    search_fields = ['user__username', 'leetcode_username']
    readonly_fields = ['last_updated']

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'group', 'message', 'timestamp']
    list_filter = ['timestamp', 'group']
    search_fields = ['user__username', 'message']
    readonly_fields = ['timestamp']
