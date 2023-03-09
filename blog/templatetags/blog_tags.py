from blog.models import Category
from django import template
from blog.models import Post
import datetime

register = template.Library()

@register.simple_tag
def hello():
    return 'Hello World'

@register.simple_tag
def publishedPosts():
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now())
    return posts

@register.simple_tag
def totalPosts():
    postCounter = Post.objects.filter(published_date__lte=datetime.datetime.now()).count()
    return postCounter

@register.filter
def snippet(text,arg=28):
    return text[:arg]#[:20] #+ '...'

@register.inclusion_tag('blog/blog-popular-posts.html')
def popularPosts(arg=3):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now()).order_by('-counted_views')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-last-posts.html')
def lastestPosts(arg=3):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now()).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postCategories():
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now())
    categories = Category.objects.all()
    post_cat_counter = {}
    for categoryItem in categories:
        post_cat_counter[categoryItem] = posts.filter(category=categoryItem).count()
    return {'post_cat_counter':post_cat_counter}