from django.db import models
from django.urls import reverse


def upload_location(instance, filename):
    return "%s/%s" % (instance.title, filename)


def document_upload_location(instance, filename):
    return "%s/%s"%(instance.syllabus, filename)


class StandingList(models.Model):
    title = models.CharField(max_length=255, unique=True)
    org_name = models.CharField(max_length=50, blank=True, null=True)
    org_address = models.CharField(max_length=50, blank=True, null=True)
    service = models.CharField(max_length=50, blank=True, null=True)
    tender_description = models.TextField()
    syllabus = models.FileField(upload_to=document_upload_location, blank=True, null=True)
    published_on = models.CharField(max_length=55, unique=True)
    published_date = models.DateTimeField()
    last_date = models.DateTimeField()
    picture = models.ImageField(upload_to=upload_location, blank=True, null=True)
    slug = models.SlugField(allow_unicode=True, unique=True, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("standinglist:all", kwargs={'slug': self.slug})


