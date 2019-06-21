from __future__ import unicode_literals
from django.db import models
from django_cleanup import cleanup
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor


@cleanup.ignore
class Mymodel(models.Model):
    width = 300
    height = 300
    resize_photo = fields.ImageField(upload_to='story1399', null=True, blank=True, dependencies=[
        FileDependency(attname='original_photo', processor=ImageProcessor(
            format='JPEG', scale={'max_width': width, 'max_height': height}))
    ])
    original_photo = models.ImageField(upload_to='story1399', null=True, blank=True)

