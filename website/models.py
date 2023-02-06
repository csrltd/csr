from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class contactMessage(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField(max_length=1000)
    date_ceated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=None)

    def __str__(self):
        return self.category
    
    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

class Blog(models.Model):
    draft = 'Draft'
    published = 'Published'
    defaul_summary = 'Lorem ipsum dolor sit amet consectetur adipiscing elit Ut et massa mi. Aliquam in hendrerit urna'
    STATUS_CHOICES = [
        (draft, 'Draft'),
        (published, 'Published'),
        ]
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=2, null=None)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='uncategorised')
    author = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=draft)
    featured_image = models.ImageField(upload_to='blog/featured_images')
    blog_summary = models.TextField(max_length=255, default=defaul_summary)
    blog_content = RichTextUploadingField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', kwargs={'slug': self.slug})
    

class Feature(models.Model):
    title = models.CharField(max_length=255)
    article_link = models.URLField(max_length=255, null=True)
    featured_image = models.ImageField(upload_to='features/featured_images')
    news_paper = models.TextField(max_length=255, default='Igihe') 
    date_featured = models.DateTimeField(auto_now_add=False, null= True)
    def __str__(self):
        return self.title