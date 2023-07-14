from django.contrib import admin
from .models import Plan, SubGoal, WayGoal, Comment

admin.site.register(Plan)
admin.site.register(SubGoal)
admin.site.register(WayGoal)
admin.site.register(Comment)
