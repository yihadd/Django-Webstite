from django.db import models
from ckeditor.fields import RichTextField # API provided by the Django CKEditor package
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
  

    def __str__(self):
        return self.title


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField() 
    session_key = models.CharField(max_length=40, unique=True)  
    visit_date = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return f"Visitor from {self.ip_address} on {self.visit_date}"