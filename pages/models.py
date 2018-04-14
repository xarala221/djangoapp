from django.db import models

# Create your models here.

LAYOUT_CHOICES = (
    ('standard', 'Standard'),
     ('stacked', 'Stacked')
                ) 

class Page(models.Model):
    title               = models.CharField(max_length=200)
    title_description   = models.CharField(max_length=200, blank=True, null=True)
    title_btn           = models.CharField(max_length=50, blank=True, null=True, default="Join")
    title_btn_url       = models.CharField(max_length=50, blank=True, null=True)
    content             = models.TextField()
    show_nav            = models.BooleanField(default=True)
    nav_color           = models.CharField(max_length=10, default="#000000")
    layout              = models.CharField(max_length=20, choices=LAYOUT_CHOICES, default="standard")
    video_embed         = models.TextField()

    def __str__(self):
        return self.title