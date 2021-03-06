from django.contrib import admin
from webapp.models import Hotel

# Register your models here.

class ModernAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'time_start', 'status']
    list_filter = ['status']
    search_fields = ['name', 'status']


admin.site.register(Hotel, ModernAdmin)
