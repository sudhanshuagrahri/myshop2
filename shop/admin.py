from django.contrib import admin
from .models import Category, Product, Profile

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'quantity', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'quantity']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'phone_no']