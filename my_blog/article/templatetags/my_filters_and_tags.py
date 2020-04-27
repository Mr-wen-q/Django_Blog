from django import template
from django.utils import timezone

import math
import datetime
register = template.Library()

# filter可以通过装饰器进行注册。若注册装饰器中携带了name参数，
# 则其值为此filter的名称；若未携带，则函数名就是filter的名称。
@register.filter(name='transfer')
def transfer(value, arg):
    """将输出转化为字符串arg"""
    return arg


@register.filter()
def lower(value):
    """将字符串转化为小写"""
    return value.lower()

# 获取相对时间
@register.filter(name='timesince_zh')
def time_since_zh(value):
    now = timezone.now()
    diff = now - value

    if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
        return '刚刚'

    if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
        return str(math.floor(diff.seconds / 60)) + "分钟前"

    if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
        return str(math.floor(diff.seconds / 3600)) + "小时前"

    if diff.days >= 1 and diff.days < 30:
        return str(diff.days) + "天前"

    if diff.days >= 30 and diff.days < 365:
        return str(math.floor(diff.days / 30)) + "个月前"

    if diff.days >= 365:
        return str(math.floor(diff.days / 365)) + "年前"

# 注册标签
@register.simple_tag
def change_http_to_https(url):
    """将http替换成https"""
    new_url = url.replace('http://', 'https://')
    return new_url
    
@register.simple_tag
def current_time(format_string):
    """回去指定格式的时间字符串"""
    return datetime.datetime.now().strftime(format_string)