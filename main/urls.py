from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path,include


app_name='main'
urlpatterns = [
    path('', views.home, name='Home'),
    path('menu', views.menu, name='Menu'),
    path('delivery', views.delivery, name='delivery'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('contact', views.contact, name='contact'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
