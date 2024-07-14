from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name_plural = 'Categories'


    

class Post(models.Model):
    category = models.ForeignKey(Category, null=True, related_name="categories", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog_image", blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    

    
