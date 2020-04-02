from . import views
from django.urls import path

# Djiango2.0必须加app_name
app_name = 'userprofile'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    # 用户退出
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    # 用户删除
    path('delete/<int:id>/', views.user_delete, name='delete'),
]
