from article import views
from django.urls import path

# Djiango2.0必须加app_name
app_name = 'article'

urlpatterns = [
    # path函数将url映射到视图, name参数对应html中调用， views对应函数调用
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-safe-delete/<int:id>', views.article_safe_delete, name='article_safe_delete'),
    path('article-update/<int:id>/', views.article_update, name='article_update'),
]