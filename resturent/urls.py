
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('menu', include('main.urls', namespace='main')),
    path('delivery', include('main.urls', namespace='main')),
    path('about', include('main.urls', namespace='main')),
    path('news', include('main.urls', namespace='main')),
    path('contact', include('main.urls', namespace='main')),


]
