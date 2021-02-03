from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title','content')
    # slug에 들어가는 값을 자동 연결?
    prepopulated_fields ={'slug':('title',)}
    # 두개를 매핑해서 등록함
admin.site.register(Post, PostAdmin)