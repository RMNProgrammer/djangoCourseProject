from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_date','published_date','counted_views')
    fields = ('title','content','published_date')
    #added to models.py
    #ordering = ['title']
    search_fields = ['title','content']
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    empty_value_display = '-No info-' 

admin.site.register(Post,PostAdmin)