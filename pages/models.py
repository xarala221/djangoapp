from django.db import models

# Create your models here.

class Page(models.Model):
    title               = models.CharField(max_length=200)
    title_description   = models.CharField(max_length=200, blank=True, null=True)
    title_btn           = models.CharField(max_length=50, blank=True, null=True, default="Join")
    title_btn_url       = models.CharField(max_length=50, blank=True, null=True)
    content             = models.TextField()