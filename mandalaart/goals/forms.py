from django import forms
from .models import WayGoal, Comment
from django.forms import formset_factory


class MainGoalForm(forms.Form):
    main_goal = forms.CharField(max_length=200)


class SubGoalForm(forms.Form):
    sub_goals = forms.CharField(widget=forms.Textarea(attrs={"rows": 9, "cols": 30}))


class WayGoalForm(forms.ModelForm):
    way_goal = forms.CharField(widget=forms.Textarea)
    way_fre = forms.IntegerField(min_value=0, max_value=30, label='목표 달성 빈도')
    way_memo = forms.CharField(widget=forms.Textarea, label='메모')

    class Meta:
        model = WayGoal
        fields = ['way_goal', 'way_fre', 'way_memo']
        

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = [
            "content",
        ]

    way_fre = forms.IntegerField(min_value=0, max_value=30, label="목표 달성 빈도")
    way_memo = forms.CharField(widget=forms.Textarea, label="메모")

    class Meta:
        model = WayGoal
        fields = ["way_goal", "way_fre", "way_memo"]


WayGoalFormSet = forms.formset_factory(
    WayGoalForm, extra=1
)  # 여러 개의 WayGoal을 입력받을 수 있는 폼셋 생성
