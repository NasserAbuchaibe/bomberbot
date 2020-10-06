from django.db import models
from datetime import datetime
from uuid import uuid4

# Create your models here.

class StudentModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    firts_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    parent = models.ForeignKey('ParentsModel', on_delete=models.CASCADE, default=None)
    teacher = models.CharField(max_length=100)
    classroom_id = models.CharField(max_length=60, unique=True)
    access_code = models.CharField(max_length=60)
    selected_course = models.CharField(max_length=60)
    owner_project = models.CharField(max_length=100)
    description_project = models.TextField()
    reference_project = models.CharField(max_length=60)
    cover_image1 = models.URLField(max_length=150)
    cover_image2 = models.URLField(max_length=150)
    last_time = models.DateTimeField(null=True, blank=True)
    total_time = models.FloatField(default=0)
    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username


class ParentsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False) 
    firts_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    
    class Meta:
        ordering = ['username']
    
    def __str__(self):
        return self.username
