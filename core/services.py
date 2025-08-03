import requests
import json
from .models import LeetCodeStats

class LeetCodeService:  
    @staticmethod
    def fetch_user_stats(leetcode_username):
        try:
            url = f"https://leetcode-stats-api.herokuapp.com/{leetcode_username}"
            print(f"[DEBUG] Fetching: {url}")  # ← add this
            response = requests.get(url, timeout=10)

            print(f"[DEBUG] Status code: {response.status_code}")
            print(f"[DEBUG] Response JSON: {response.json()}")  # ← print full response

            if response.status_code == 200:
                data = response.json()
                return {
                    'global_ranking': data.get('ranking'),
                    'total_solved': data.get('totalSolved', 0),
                    'easy_solved': data.get('easySolved', 0),
                    'medium_solved': data.get('mediumSolved', 0),
                    'hard_solved': data.get('hardSolved', 0),
                }
            return None
        except Exception as e:
            print(f"Error fetching stats for {leetcode_username}: {e}")
            return None



    
    @staticmethod
    def update_user_stats(user_stats_obj):
        """Update user stats in database"""
        stats_data = LeetCodeService.fetch_user_stats(user_stats_obj.leetcode_username)
        if stats_data:
            user_stats_obj.global_ranking = stats_data['global_ranking']
            user_stats_obj.total_solved = stats_data['total_solved']
            user_stats_obj.easy_solved = stats_data['easy_solved']
            user_stats_obj.medium_solved = stats_data['medium_solved']
            user_stats_obj.hard_solved = stats_data['hard_solved']
            user_stats_obj.save()
            return True
        return False
    
    @staticmethod
    def update_all_stats():
        """Update stats for all users"""
        for stats in LeetCodeStats.objects.all():
            LeetCodeService.update_user_stats(stats)
