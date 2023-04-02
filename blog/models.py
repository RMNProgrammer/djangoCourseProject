from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    #status = models.BooleanField(default=False)
    login_require = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'post timeline'
        verbose_name_plural = 'posts timeline'

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return reverse('blog:posts',kwargs={'PostID':self.id})

    #def snippets(self):
    #    return self.content[:27] + '...'

class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.TextField(max_length=80)
    message = models.TextField(max_length=80)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.subject