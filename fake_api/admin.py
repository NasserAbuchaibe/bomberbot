from django.contrib import admin
from .models import StudentModel, ParentsModel
# Register your models here.

admin.site.register(StudentModel)
admin.site.register(ParentsModel)