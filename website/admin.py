from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(contactMessage)
class contactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')

@admin.register(Blog)
class blogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'date_created', 'status')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Feature)
class featureAdmin(admin.ModelAdmin):
    list_display = ('news_paper', 'title', 'date_featured')

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('category','slug')
    prepopulated_fields = {"slug": ("category",)}