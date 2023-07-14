
from django.contrib import admin
from django.urls import path , include
from accounts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('goals/', include('goals.urls', namespace='goals')),
]
