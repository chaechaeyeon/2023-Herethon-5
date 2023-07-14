from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import validate_email


# 회원가입폼
class SignupForm(UserCreationForm):
    class Meta:
        first_name = forms.CharField(max_length=30, required=True, label="이름")

        model = User
        fields = ("username", "first_name", "password1", "password2")

    # username을 email로 설정
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].validators = [validate_email]
        self.fields["username"].help_text = "이메일 형식을 입력하세요."
        self.fields["username"].label = "Email"

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = user.username
        if commit:
            user.save()
        return user
