from django.contrib import admin
from .models import Category, Property

@admin.register(Property)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category','image')

@admin.register(Category)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','image')




