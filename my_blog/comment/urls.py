from . import views
from django.urls import path


app_name = 'comment'

urlpatterns = [
    # 一级回复
    path('post-comment/<int:article_id>', views.post_comment, name='post_comment'),
    path('post-comment/<int:article_id>/<int:parent_comment_id>',
         views.post_comment, name='comment_reply'),
]