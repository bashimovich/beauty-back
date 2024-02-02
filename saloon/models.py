from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify
# from slugify import slugify
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from ckeditor.fields import RichTextField


COMPANY_TYPE = [
    ("df", "Default"),
    ("top", "Top"),
    ("wtv", "Worth to visit"),
]

class WebImage(models.Model):
    src = models.ImageField(upload_to="web_images")
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def img_preview(self):
        return mark_safe(f'<img src="{self.src.url}" width=70 height=70>')

class MobileImage(models.Model):
    src = models.ImageField(upload_to="mobile_images")
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def img_preview(self):
        return mark_safe(f'<img src="{self.src.url}" width=70 height=70>')
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    description = RichTextField(null=True)
    _type = models.CharField(max_length=3, null=True, default='df', choices=COMPANY_TYPE)

    web_images = GenericRelation('WebImage', blank=True, null=True)
    mobile_images = GenericRelation('MobileImage', blank=True, null=True)
    is_active  = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    


class Workers(models.Model):
    name = models.CharField(max_length=255, null=True)
    job = models.CharField(max_length=255, null=True)

    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='workers', null=True)

    web_images = GenericRelation('WebImage', blank=True, null=True)
    mobile_images = GenericRelation('MobileImage', blank=True, null=True)
    is_active  = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Services(models.Model):
    name = models.CharField(max_length=255, null=True)
    _type = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    delay = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='services', null=True)

    web_images = GenericRelation('WebImage', blank=True, null=True)
    mobile_images = GenericRelation('MobileImage', blank=True, null=True)
    is_active  = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Order(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='orders', null=True)
    date = models.CharField(max_length=255, null=True)
    time = models.CharField(max_length=255, null=True)
    service = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 