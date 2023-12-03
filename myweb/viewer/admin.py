from django.contrib import admin
from .models import Category, Property, Order

@admin.register(Property)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'image')


@admin.register(Category)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')


@admin.register(Order)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'id', 'date_from', 'date_to', 'email', 'address', 'city', 'postal')




