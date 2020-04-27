from django.urls import path
from notice import views

app_name = 'notice'

urlpatterns = [
    # 通知列表
    path('list/', views.CommentNoticeListView.as_view(), name='list'),
    # 更新通知状态
    path('update/', views.CommentNoticeupdateView.as_view(), name='update'),
    # 历史通知
    path('history/', views.CommentNoticeHistoryView.as_view(), name='history'),

]