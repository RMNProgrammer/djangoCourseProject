from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category
from django.contrib import admin

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title','author','created_date','published_date','counted_views')
    fields = ('author','title','category','tags','content','image','published_date')
    summernote_fields = ('content',)
    #added to models.py
    #ordering = ['title']
    search_fields = ['title','content']
    list_filter = ('created_date','author')
    date_hierarchy = 'created_date'
    empty_value_display = '-No info-' 

admin.site.register(Category)
admin.site.register(Post,PostAdmin)