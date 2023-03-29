from django.contrib.syndication.views import Feed
from blog.models import Post
import datetime

class LastestEntriesFeed(Feed):
    title = "Blog newest posts"
    link = "/rss/"
    description = "Best blog ever"

    def items(self):
        return Post.objects.filter(published_date__lte=datetime.datetime.now())

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:60]