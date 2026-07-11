from django.db import models
from pytils.translit import slugify
from django.contrib.auth.models import User 
from django.urls import reverse

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=200)
    info = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_time = models.TimeField(blank=True, null=True)
    image = models.ImageField(upload_to="task_images", blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    name = models.CharField(max_length=200)
    info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="note_images", blank=True, null=True)
    slug = models.SlugField()


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse('main:note', kwargs={'slug': self.slug})


    def __str__(self):
        return self.name
