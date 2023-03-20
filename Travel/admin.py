from django.contrib import admin
from Travel.models import Contact, Newsletter

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['subject','name','created_date']
    list_filter = ['email']
    search_fields = ['name','subject']
    
admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter)