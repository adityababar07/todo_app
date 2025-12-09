from django.conf import settings
from django.contrib.auth import get_user_model
import accounts
from accounts.models import CustomUser
from django.db import models
from django.urls import reverse

# Create your models here.

global primary_key

class ToDo(models.Model):
    title = models.CharField(max_length=200)
    author_id = CustomUser.id
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )
    CATEGORY_CHOICES = (
        ('Knowledge', 'Knowledge'),
        ('Idea', 'Idea'),
        ('Question', 'Question'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Knowledge')
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        primary_key = str(self.pk)
        return reverse('todo_detail', args=[primary_key])
    class Meta:
        ordering = ('-date',)

class Comment(models.Model):
    todo = models.ForeignKey(
        ToDo,
        on_delete = models.CASCADE,
        related_name = 'comments',
        )
    comment = models.CharField(max_length=140)
    comment_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )
    class Meta:
        ordering = ["comment_date"]

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('todo_detail', args=[primary_key])
