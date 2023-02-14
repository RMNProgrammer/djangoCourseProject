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
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'post timeline'
        verbose_name_plural = 'posts timeline'

    def __str__(self):
        return "{}".format(self.title)