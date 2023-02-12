from django.db import models

class Post(models.Model):
    #image
    #author
    title = models.CharField(max_length=255)
    content = models.TextField()
    #category
    #tag
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_data = models.DateTimeField(null=True)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)