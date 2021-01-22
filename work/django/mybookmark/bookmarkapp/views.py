from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmarkapp.models import Bookmark
# Create your views here.
'''
ListView.py 내에
    object_list = SELECT * FROM bookmark;
이런 형식으로 저장되어 있는 것

DetailView.py 의 경우
    object = SELECT *FROM bookmark WHERE id=?;
'''
class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark