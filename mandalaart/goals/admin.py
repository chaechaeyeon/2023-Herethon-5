from django.contrib import admin
from . import models

admin.site.register(models.Plan)
admin.site.register(models.SubGoal)
admin.site.register(models.WayGoal)