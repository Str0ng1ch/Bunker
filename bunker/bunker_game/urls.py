from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("register/", views.register_page, name="register"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.profile, name="profile"),
    path('created_version/', views.created_version, name='created_version'),
    path('generate_version/', views.generate_version, name='generate_version'),
    path('check_results/', views.check_results, name='check_results'),
]
