import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_image = models.CharField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=20, null=False, unique=True)
    name = models.CharField(max_length=30, null=False, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    standard = models.PositiveIntegerField(null=True, blank=True)
    division = models.CharField(max_length=1, null=True, blank=True)
    house = models.CharField(max_length=20, null=True, blank=True)
    stream = models.CharField(max_length=20, null=True, blank=True)
    school = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])


class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(CustomUser, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower.username} follows {self.following.username}'
