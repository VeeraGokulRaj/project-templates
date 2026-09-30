from django.contrib import admin
from {{ cookiecutter.app_name }}.models import BackgroundTask, BackgroundTaskEvent


@admin.register(BackgroundTask)
class BackgroundTaskAdmin(admin.ModelAdmin):
    list_display = ("name", "task_id", "status", "created_by", "created", "finished_at")
    list_filter = ("status", "queue")
    search_fields = ("name", "task_id")


@admin.register(BackgroundTaskEvent)
class BackgroundTaskEventAdmin(admin.ModelAdmin):
    list_display = ("task", "event", "message", "created")
    list_filter = ("event",)
    search_fields = ("task__name", "message")
