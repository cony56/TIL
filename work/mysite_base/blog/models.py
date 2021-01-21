from django.db import models
from django.urls import reverse
# Create your models here.
# print() -> {{}}
# print할 때 title이 나오게 됨
class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True,
    help_text= 'one word for this alias')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True,
    help_text='simple description text')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)

    def __str__(self):
        return self.title
        #Post 클래스 내부에 만드는 inner class
        # 데이터베이스와 연관된 정보를 만드는게 모델 클래스임
        # 사용자가 변경하고 싶은 데이터가 있는 경우 메타클래스에 정의해서
        # 사용할 수 있음
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        #정렬상태 (내림차순)
        #ordering = ('modify_date',)    # ascending
        ordering = ('-modify_date',)    # descending
        #ordering = ('-modify_date', author) #이렇게 다른 기준 추가 가능
    
    #<a>와 관련된 
    # 링크를 template페이지에서도 처리할 수 있지만 모델 클래스 내에
    # 정의했을 때 -> 원하는 디테일 페이지로 이동할 수 있음
    def get_absolute_url(self):
        # reverse란
        #장고에서 사용하는 url 표기법 -> 실제 url 형태로 바꿔주는 기능을 함
        # 파이썬에서 'blog:post_detail' 실행하면 blog/post/django~~이렇게 바뀜
        return reverse('blog:post_detail', args=(self.slug,))
    
    def get_previous_post(self):
        return self.get_previous_by_modify_date()
    
    def get_next_post(self):
        return self.get_next_by_modify_date()
        