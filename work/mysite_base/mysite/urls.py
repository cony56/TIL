from django.contrib import admin
from django.urls import path, include
from mysite.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    #http://127.0.0.1:8000/ -> home page
    path('', HomeView.as_view(), name = 'home'),
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('blog/', include('blog.urls', namespace='blog')),
]
