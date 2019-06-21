from django.contrib import admin
from .models import Mymodel
# Register your models here.


@admin.register(Mymodel)
class MymodelAdmin(admin.ModelAdmin):
    model = Mymodel
