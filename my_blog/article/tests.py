from django.test import TestCase

import datetime
from django.utils import timezone
from article.models import ArticlePost
from django.contrib.auth.models import User
# Create your tests here.


class ArticlePostModelTests(TestCase):

    def test_was_created_recently_with_future_article(self):
        # 若文章创建时间为未来，返回False
        author = User(username='abcd', password='test_password')
        author.save()

        future_article = ArticlePost(
            author=author,
            title='test1',
            body='test1',
            created=timezone.now() + datetime.timedelta(days=30)
        )

        self.assertIs(future_article.was_created_recently(), False)