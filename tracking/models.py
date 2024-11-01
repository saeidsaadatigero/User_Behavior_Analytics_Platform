# tracking/models.py
from django.db import models

class UserBehavior(models.Model):
    user_id = models.IntegerField()
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(blank=True, null=True)  # برای ذخیره اطلاعات اضافی

    def __str__(self):
        return f"User {self.user_id} - {self.action} at {self.timestamp}"
