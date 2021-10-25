from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Qrcode(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name


class Qrfilecode(models.Model):
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='name')
    uploads = models.FileField(upload_to='img/imgs')
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    class Meta:
        ordering = ('-name',)

    def get_absolute_url(self):
        return reverse('qrDisplay',args=[self.slug])

    def __str__(self):
        return self.name

    def get_upload(self):
        if self.uploads and hasattr(self.uploads, 'url'):
            return self.uploads.url

class Qraudiocode(models.Model):
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='name')
    uploads = models.FileField(upload_to='img/audios')
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    class Meta:
        ordering = ('-name',)

    def get_absolute_url(self):
        return reverse('qraudioDisplay',args=[self.slug])

    def __str__(self):
        return self.name

    def get_upload(self):
        if self.uploads and hasattr(self.uploads, 'url'):
            return self.uploads.url

class Qrpdfcode(models.Model):
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='name')
    uploads = models.FileField(upload_to='img/pdfs')
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    class Meta:
        ordering = ('-name',)

    def get_absolute_url(self):
        return reverse('qrpdfDisplay',args=[self.slug])

    def __str__(self):
        return self.name

    def get_upload(self):
        if self.uploads and hasattr(self.uploads, 'url'):
            return self.uploads.url


