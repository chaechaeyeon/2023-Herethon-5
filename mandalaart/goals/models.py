from django.db import models

class Plan(models.Model):
    main_goal = models.CharField(max_length=200)
    
    def __str__(self):
        return self.main_goal

class SubGoal(models.Model):
    plan = models.ForeignKey(Plan, related_name='sub_goals', on_delete=models.CASCADE)
    sub_goal = models.CharField(max_length=200)
    
    def __str__(self):
        return self.sub_goal

class WayGoal(models.Model):
    sub = models.ForeignKey(SubGoal, on_delete=models.CASCADE)
    way_goal = models.CharField(max_length=200)
    
    def __str__(self):
        return self.way_goal