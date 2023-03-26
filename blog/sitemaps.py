from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post
import datetime

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Post.objects.filter(published_date__lte=datetime.datetime.now())

    def lastmod(self,item):
        return item.published_date

    #def location(self, item):
    #    return reverse('blog:posts',kwargs={'PostID':item.id})