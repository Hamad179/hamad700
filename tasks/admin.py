from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('العنوان', 'مكتملة')
    list_filter = ('مكتملة',)
    search_fields = ('العنوان',)
