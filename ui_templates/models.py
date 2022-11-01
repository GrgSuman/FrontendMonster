from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse

class TemplateCategory(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(default="")
    keywords = models.CharField(max_length=400,default="")
    metaDesc = models.CharField(max_length=400,default="")
    featuredImage = models.ImageField(default="defaultBG.png",upload_to="uploads/images")

    def __str__(self):
        return self.name

class Template(models.Model):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(default="")
    featuredImage = models.ImageField(default="defaultBG.png",upload_to="uploads/images")
    keywords = models.CharField(max_length=400,default="")
    metaDesc = models.CharField(max_length=400,default="")
    category = models.ForeignKey(TemplateCategory,on_delete=models.PROTECT,related_name="template_collection",null=True,blank=True)
    body  =    HTMLField(blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.PROTECT)
    createdAt = models.DateTimeField(null=True)
    updated = models.BooleanField(default=False)
    postStatus = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogDetail', args=[str(self.slug)])
