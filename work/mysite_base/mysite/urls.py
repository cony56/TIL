from django.contrib import admin
from django.urls import path, include
from mysite.views import HomeView

# from rest_framework import routers
# from blog import rest_views

# router = routers.DefaultRouter()
# router.register(r'users',rest_views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    #http://127.0.0.1:8000/ -> home page
    path('', HomeView.as_view(), name = 'home'),
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('blog/', include('blog.urls', namespace='blog')),
    #path('api/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('api/', include('api.urls',namespace='api')),
]
