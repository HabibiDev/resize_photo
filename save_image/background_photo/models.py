from __future__ import unicode_literals
from django.db import models
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
from .image_sizes import CONSUMER_BACKGROUND_WIDTH, CONSUMER_BACKGROUND_HEIGHT


class Mymodel(models.Model):
    resize_photo = fields.ImageField(upload_to='story1399', null=True, blank=True, dependencies=[
        FileDependency(attname='original_photo', processor=ImageProcessor(
            format='JPEG', scale={'max_width': CONSUMER_BACKGROUND_WIDTH, 'max_height': CONSUMER_BACKGROUND_HEIGHT}))
    ])
    original_photo = models.ImageField(upload_to='story1399', null=True, blank=True)

