from django.core.management.base import BaseCommand
from core.services import LeetCodeService

class Command(BaseCommand):
    help = 'Update LeetCode stats for all users'
    
    def handle(self, *args, **options):
        self.stdout.write('Starting LeetCode stats update...')
        LeetCodeService.update_all_stats()
        self.stdout.write(
            self.style.SUCCESS('Successfully updated all LeetCode stats')
        )
