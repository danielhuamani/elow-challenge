from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Events


class EventsAdmin(SummernoteModelAdmin):
    exclude = ["is_delete"]
    summernote_fields = ("description",)


admin.site.register(Events, EventsAdmin)
