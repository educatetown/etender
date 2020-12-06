from django.db import models


def upload_location(instance, filename):
    return "%s/%s"%(instance.title, filename)


BANNER_SIZE_CHOICES = (
        ('Half', 'half'),
        ('Quarter', 'quarter'),
        ('Full', 'full'),
    )


PLACE_CHOICES = (
    ('HomeTop', 'hometop'),
    ('HomeMiddle', 'homemiddle'),
    ('HomeBottom', 'homebottom'),
    ('HomeRight', 'homeright'),
    ('SingleTop', 'singletop'),
    ('SingleRight', 'singleright'),
    ('SingleBottom', 'singlebottom'),
)


class AdvertisingInfo(models.Model):
    name = models.CharField(max_length=50)
    banner_size = models.CharField(choices=BANNER_SIZE_CHOICES, default='Half', max_length=15)
    email = models.EmailField(blank=True, null=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    organization = models.CharField(max_length=45, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


class Advertising(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to=upload_location, null=True)
    banner_size = models.CharField(choices=BANNER_SIZE_CHOICES, default='Half', max_length=15)
    choose_place = models.CharField(choices=PLACE_CHOICES, default='HomeTop', max_length=30)
    link = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
