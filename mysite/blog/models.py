from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

options = (
    ('draft','Draft'),
    ('published','Published'),
)

class Post(models.Model):

    class newManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish_date')
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')

    def excerpt(self, length=100):
        return self.content[:length]

    #creating a custom manager to filter some stuff 
    new_manager = newManager()

    #generating an url to form links
    #this function refers to single_post as it takes slug as arg
    #this returns url of a view in view.py
    #each view will have unique url
    def get_absolute_url(self):
        return reverse('blog:single_post', args=[self.slug])
        #"blog/first-title" is one probable url

    class Meta():
        ordering = ['-publish_date']

    def __str__(self):
        return self.title