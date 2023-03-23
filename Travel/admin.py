from django.contrib import admin
from Travel.models import Contact, Newsletter

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = [Contact.__str__,'subject','name','created_date']
    empty_value_display = '-empty-'
    list_filter = ['email']
    search_fields = ['name','subject']
    
admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter)