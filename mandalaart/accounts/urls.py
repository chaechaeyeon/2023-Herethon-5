from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/', views.signup, name='signup'),
    path('successJoin/',views.successJoin, name="successJoin"),
]