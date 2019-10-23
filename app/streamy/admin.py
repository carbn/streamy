from django.contrib import admin

from .models import Stream


@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'started_at', 'live')
    readonly_fields = ('url',)
