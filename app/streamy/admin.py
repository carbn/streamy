from django.contrib import admin

from .models import Stream


@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'updated_at', 'is_live',)

    def get_readonly_fields(self, request, obj=None):
        fields = ['updated_at']

        if obj:
            fields.append('url')

        return fields

    def is_live(self, obj):
        return obj.is_live

    is_live.boolean = True
