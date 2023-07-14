from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):
    main_goal = models.CharField(max_length=200)

    def __str__(self):
        return self.main_goal

    def get_absolute_url(self):
        return f"/goals/3x3_table/{self.pk}/"


class SubGoal(models.Model):
    plan = models.ForeignKey(Plan, related_name="sub_goals", on_delete=models.CASCADE)
    sub_goal = models.CharField(max_length=200)

    def __str__(self):
        return self.sub_goal


class WayGoal(models.Model):
    sub = models.ForeignKey(SubGoal, on_delete=models.CASCADE)
    way_goal = models.CharField(max_length=200)
    way_fre = models.IntegerField(null=True)        # 목표 달성 빈도
    way_memo = models.TextField()       # 메모 
    
    def __str__(self):
        return self.way_goal


class Comment(models.Model):
    sub_goal = models.ForeignKey(SubGoal, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}::{self.content}"
