from django.views.generic import ListView, DetailView
from django.views.generic import ArchiveIndexView, YearArchiveView
from django.views.generic import MonthArchiveView, DayArchiveView, TodayArchiveView
from blog.models import Post

from blog.forms import PostSearchForm
from django.views.generic.edit import FormView
from django.db.models import Q
from django.shortcuts import render
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

class SearchFormView(FormView):
    form_class = PostSearchForm # forms.py에 생성
    template_name = "blog/post_search.html"

    def form_valid(self, form):
        schword = self.request.POST['search_word']
        
        post_list = Post.objects.filter(Q(title__icontains=schword) | Q(description__icontains=schword) | Q(content__icontains=schword)).distinct()
        #검색된 결과
        context = {}
        #form 객체 -> form.as_table의 객체(검색창)
        context['form'] = form
        context['search_keyword'] = schword
        context['search_list'] = post_list

        print(post_list)
        return render(self.request, self.template_name, context)