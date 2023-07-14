from django.shortcuts import render, redirect
from django.contrib import auth
import os
from .forms import SignupForm


# 회원가입
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # auth.login(request, new_user)
            print("회원가입 성공")
            return redirect("accounts:successJoin")
    else:
        form = SignupForm()
    return render(request, "join.html", {"form": form})
 
 #회원가입 성공 
def successJoin(request):
    return render(request,'successJoin.html')

# 로그인
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print("로그인 성공")
            return render(request, "maingoal.html")
        else:
            return render(request, "bad_login.html")
    else:
        return render(request, "login.html")


# 로그아웃
def logout(request):
    auth.logout(request)
    return render(request, "login.html")
