from django.contrib import admin
from bookmarkapp.models import Bookmark
# Register your models here.

class BookmarkAdmin(admin.ModelAdmin):
    #포함하고자 하는 화면의 목록을 추가할 수 있음
    list_display = ('title','url')

admin.site.register(Bookmark, BookmarkAdmin)
