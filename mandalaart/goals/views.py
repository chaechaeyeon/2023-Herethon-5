from django.shortcuts import render, redirect
from django.contrib import auth

#5-1 목표 확인_만다라트 형식
def mainpage(request) :

    return render(request, 'mainmanadal.html')