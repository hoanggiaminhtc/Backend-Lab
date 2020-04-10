from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.
class News(models.Model):
    title   = models.CharField(max_length=1000)
    #slug    = models.SlugField(unique=True)
    content = models.TextField(null=True)
    image   = models.ImageField(default='about.png',blank=True,null=True)
    author  = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    image_2= models.ImageField(null=True,blank=True)
    image_3= models.ImageField(null=True,blank=True)
    image_4= models.ImageField(null=True,blank=True)
    #views = models.IntegerField(default=0,null=True)
    date    = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return "/news/%" %(self.id) #f"/products/{self.id}/"
    def snippet(self):
        return self.content[:100] + '...'
    def __str__(self):
        return self.title
class Comment(models.Model):
    post    = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    body    = models.TextField(null=False)
    date    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return'{}-{}'.format(self.post.title,str(self.author.username))

