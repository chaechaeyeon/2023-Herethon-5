from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login, name="login"),
    path("accounts/", include("accounts.urls", namespace="account")),
    path("goals/", include("goals.urls")),
    path("authaccounts/", include("allauth.urls")),
]
