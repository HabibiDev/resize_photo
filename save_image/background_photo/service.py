import StringIO
from django.core.files import File
from django.db import models
from django.db.models.fields.files import ImageFieldFile


class ResizeOldImage(object):

    def __init__(self, field, instance):
        self.model_field = str(field)
        self.model_object = instance

    def check_field(self):
        if self.model_field not in self.model_object.__dict__.keys():
            raise KeyError

    def is_image(self):
        if not isinstance(self.model_object.__getattribute__(self.model_field), ImageFieldFile):
            raise TypeError

    def get_field(self):
        return self.model_object.__getattribute__(self.model_field)

    def resize(self):
        self.check_field()
        self.is_image()
        image = self.get_field()
        if image:
            output = StringIO.StringIO(self.model_object.__getattribute__(self.model_field).read())
            output.seek(0)
            self.model_object.resize_photo = File(output, image.name)
            self.model_object.save()


class AllModelsImageResize(object):
    def __init__(self, field, Model):
        self.model = Model
        self.model_field = field

    def check_model_instance(self):
        if not issubclass(self.model, models.Model):
            raise TypeError

    def get_model_objects(self):
        return self.model.objects.all()

    def resize_all_images(self):
        self.check_model_instance()
        objects = self.get_model_objects()
        for obj in objects:
            res = ResizeOldImage(self.model_field, obj)
            res.resize()
