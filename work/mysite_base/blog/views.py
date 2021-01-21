from django.views.generic import ListView, DetailView
from django.views.generic import ArchiveIndexView, YearArchiveView
from django.views.generic import MonthArchiveView, DayArchiveView, TodayArchiveView
from blog.models import Post

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts' #object_list -> 북마크의 목록 정리
    # 페이지에 들어갈 post수 지정하기
    paginate_by = 3

class PostDV(DetailView):
    model = Post
    
class PostAV(ArchiveIndexView):
    model = Post
    # 날짜 관련된 필드
    # modify_date는 날짜 변경할 수 있음
    date_field ="modify_date"

class PostYAV(YearArchiveView):
    model = Post
    date_field ="modify_date"
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field ="modify_date"
    month_format = "%m"
class PostDAV(DayArchiveView):
    model = Post
    date_field ="modify_date"
    month_format = "%m"
class PostTAV(TodayArchiveView):
    model = Post
    date_field ="modify_date"
    month_format = "%m"
