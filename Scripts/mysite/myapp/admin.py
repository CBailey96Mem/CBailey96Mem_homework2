from django.contrib import admin
from .models import MyModel
from .models import MyOtherModel

# Register your models here.

admin.site.register(MyModel)
admin.site.register(MyOtherModel)