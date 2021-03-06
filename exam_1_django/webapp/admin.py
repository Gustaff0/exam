from django.contrib import admin
from webapp.models import Hotel

# Register your models here.

class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'time_start', 'status', 'time_edit']
    list_filter = ['status']
    search_fields = ['name', 'status']


admin.site.register(Hotel, ListAdmin)
