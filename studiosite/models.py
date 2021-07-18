from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
import PIL
import datetime
# Create your models here.

class gallery(models.Model):
    img = models.ImageField()
    thumb = ImageSpecField(source='img', processors=[ResizeToFit(500)], format='JPEG', options={'quality': 70})




class Feedback(models.Model):
    Name = models.CharField(max_length=100)
    Instagram_handle = models.CharField(max_length=1000, null = True, blank=True)
    MY_CHOICES = (
        ('BRIDAL MAKEUP', 'BRIDAL MAKEUP'),
        ('SKIN CONSULTANCY', 'SKIN CONSULTANCY'),
        ('PARTY MAKEUP', 'PARTY MAKEUP'),
        ('SELF GROOMING', 'SELF GROOMING'),
        ('PROFESSIONAL MAKEUP COURSE', 'PROFESSIONAL MAKEUP CLASS'),
        ('EVENT MAKEUP', 'EVENT MAKEUP'),
    )
    Makeup = models.CharField(max_length=100, choices=MY_CHOICES)
    Image = models.ImageField(null=True, blank=True)
    Feedback = models.TextField(max_length= 1000,null=True,blank=True)

#
class Reveiw(models.Model):
    MY_CHOICES = (
        ('BRIDAL MAKEUP', 'BRIDAL MAKEUP'),
        ('SKIN CONSULTANCY', 'SKIN CONSULTANCY'),
        ('PARTY MAKEUP', 'PARTY MAKEUP'),
        ('SELF GROOMING', 'SELF GROOMING'),
        ('PROFESSIONAL MAKEUP COURSE', 'PROFESSIONAL MAKEUP CLASS'),
        ('EVENT MAKEUP', 'EVENT MAKEUP'),
    )
    Name_reveiw = models.CharField(max_length=100, null=True, blank=True),
    Makeup_reveiw = models.CharField(max_length=100, choices=MY_CHOICES)
    Reveiw_field = models.TextField(max_length=1000)
