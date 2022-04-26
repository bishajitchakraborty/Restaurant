from django.contrib import admin
from .models import Branch, Menu, News, Home, About, Gallery


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['id','branch']


@admin.register(Menu)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['id','title','subTitle','price','image']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','title','date','image','description']


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','image']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id','title','name','description','image']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id','image']

