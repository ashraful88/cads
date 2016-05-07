from django.contrib import admin
from . import models
from django.db.models import TextField
# Register your models here.

class EntryAdmin(admin.ModelAdmin):
	list_display = ("title", "created")
	prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
	list_display = ("title", "parent")
	prepopulated_fields = {"slug": ("title",)}	

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag)