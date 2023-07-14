from django import forms
from .models import WayGoal, Comment
from django.forms import formset_factory


class MainGoalForm(forms.Form):
    main_goal = forms.CharField(max_length=200)


class SubGoalForm(forms.Form):
    sub_goals = forms.CharField(widget=forms.Textarea(attrs={"rows": 9, "cols": 30}))


class WayGoalForm(forms.ModelForm):
    way_goal = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = WayGoal
        fields = ["way_goal"]


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = [
            "content",
        ]
