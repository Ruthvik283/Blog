from django.db import models

# Create your models here.

class Blogs(models.Model):
    category = models.ForeignKey("BlogCategory", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=191,null=True)
    description = models.CharField(max_length=191,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class BlogCategory(models.Model):
    name = models.CharField(max_length=191,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    