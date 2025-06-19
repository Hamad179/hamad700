from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_completed')
    list_filter = ('is_completed',)
    search_fields = ('title',)
