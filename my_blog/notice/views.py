from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from article.models import ArticlePost

# 导入日志
from my_blog.settings import LOGGING
import logging
# Create your views here.


class CommentNoticeListView(LoginRequiredMixin, ListView):
    """通知列表"""
    # 上下文
    context_object_name = 'notices'
    # 模板位置
    template_name = 'notice/list.html'
    # 登录重定向(必须登录操作)
    login_url = '/userprofile/login/'

    # 未读通知查询
    def get_queryset(self):
        return self.request.user.notifications.unread()


class CommentNoticeupdateView(View):
    """更新通知状态"""
    # 处理get请求

    def get(self, request):
        # 获取未读消息
        notice_id = request.GET.get('notice_id')
        # 更新单条通知
        if notice_id:
            article = ArticlePost.objects.get(id=request.GET.get('article_id'))
            request.user.notifications.get(id=notice_id).mark_as_read()
            return redirect(article)
        # 更新全部通知
        else:
            request.user.notifications.mark_all_as_read()
            return redirect('notice:list')


class CommentNoticeHistoryView(LoginRequiredMixin, ListView):
    """获取历史通知"""
    # 上下文
    context_object_name = 'notices'
    # 模板位置
    template_name = 'notice/list.html'
    # 登录重定向(必须登录操作)
    login_url = '/userprofile/login/'

    def get_queryset(self):
        return self.request.user.notifications.read()


logging.config.dictConfig(LOGGING)
logger = logging.getLogger('django.request')
def logsomething(request):
    logger.warning('something')