from . import views
from django.urls import path


app_name = 'comment'

urlpatterns = [
   path('comment/<int:article_id>', views.post_comment, name='post_comment'), 
]


