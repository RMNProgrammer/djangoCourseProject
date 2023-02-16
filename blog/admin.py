from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_date','published_date','counted_views')
    fields = ('author','title','category','content','image','published_date')
    #added to models.py
    #ordering = ['title']
    search_fields = ['title','content']
    list_filter = ('created_date','author')
    date_hierarchy = 'created_date'
    empty_value_display = '-No info-' 

admin.site.register(Category)
admin.site.register(Post,PostAdmin)