from django.db import models
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth


class Vangouser(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    username = models.CharField(blank=True, max_length=100)
    profile_picture = models.CharField(blank=True, max_length=100)
    followed_by = models.CharField(blank=True, max_length=100)
    media = models.CharField(blank=True, max_length=100)
    follows = models.CharField(blank=True, max_length=100)
    bio = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Informacion extra'
        verbose_name_plural = 'Informacion extra'
