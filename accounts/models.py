from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse


def upload_location(instance, filename):
    return "%s/%s" % (instance.user, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True, null=True)
    mobile_number = models.CharField(max_length=13, null=True, blank=True)
    profile_pic = models.ImageField(upload_to=upload_location, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("profiles:detail", kwargs={'username': self.user.username})

    def __str__(self):
        return self.user.username