from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index_user, name="index"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('edit/', views.edit_user, name="edit"),
]
