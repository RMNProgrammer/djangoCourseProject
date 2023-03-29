from blog.models import Category
from blog.models import Post, Comment
from django import template
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

@register.simple_tag(name='comments_count')
def function(PostID):
    return Comment.objects.filter(post=PostID,approved=True).count()

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

@register.inclusion_tag('website/index-recent-blog.html')
def recentBlog(arg=6):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now()).order_by('-published_date')[:arg]
    return {'last_posts':posts}