from django.urls import path
from blog.views import *
app_name = 'blog'
urlpatterns = [

    path('', PostLV.as_view(), name='index'),
    # /blog/post
    path('post/', PostLV.as_view(), name='post_list'),

    # /blog/post/({python-programming})
    path('post/<str:slug>',PostDV.as_view(), name='post_detail'),
    # /blog/archive
    path('archive/',PostAV.as_view(), name='post_archive'),
    # /2021/
    path('<int:year>/',PostYAV.as_view(), name='post_year_archive'),
    # /blog/2018/nov
    path('<int:year>/<str:month>/', PostMAV.as_view(), name='post_month_archive'),
    # Example: /2021/01/21/
    path('<int:year>/<str:month>/<int:day>/', PostDAV.as_view(), name='post_day_archive'),
    # /blog/2018/nov/12,day/ -> http://127.0.0.1:8000/blog/today/
    path('today/', PostTAV.as_view(),name='post_today_archive'),
]
