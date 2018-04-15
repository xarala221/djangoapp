from django.db import models
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError

# Create your models here.

LAYOUT_CHOICES = (
    ('standard', 'Standard'),
     ('stacked', 'Stacked')
                )
from pages.utils import unique_slug_generator

def layout_validation(value):
    if value[0] != '#':
        raise ValidationError("Must begin with #")
    if len(value) == 4 or len(value) == 7:
        return value
    raise ValidationError("Incorrect length")
class Page(models.Model):
    title               = models.CharField(max_length=200)
    title_description   = models.CharField(max_length=200, blank=True, null=True)
    title_btn           = models.CharField(max_length=50, blank=True, null=True, default="Join")
    title_btn_url       = models.CharField(max_length=50, blank=True, null=True)
    content             = models.TextField()
    slug                = models.SlugField(default="page-slug", blank=True)
    show_nav            = models.BooleanField(default=True)
    nav_color           = models.CharField(max_length=7, default="#000000", validators = [layout_validation])
    layout              = models.CharField(max_length=20, choices=LAYOUT_CHOICES, default="standard")
    video_embed         = models.TextField(blank=True, null=True)
    featured            = models.BooleanField(default=False)
    active              = models.BooleanField(default=True)
    leave_capture       = models.BooleanField(default=True)

    def save(self, *args, **kwrgs):
        if self.featured:
            qs = Page.objects.filter(featured=True).exclude(pk=self.pk)
            if qs.exists():
                qs.update(featured=False)
        super(Page, self).save(*args, **kwrgs)

    def __str__(self):
        return self.title

def pre_save_receiver_page_model(sender, instance, *args, **kwrgs):
    if instance.slug == "page-slug" or instance.slug == "":
       instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver_page_model, sender=Page)