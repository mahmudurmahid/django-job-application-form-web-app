from django.contrib import admin
from .models import Form

# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date', 'employment_status')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('date', 'employment_status')
    ordering = ('first_name',)
    readonly_fields = ('employment_status',) # Cannot change this field in the admin interface


admin.site.register(Form, FormAdmin)
