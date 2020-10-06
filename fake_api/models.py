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
    owner_project1 = models.CharField(max_length=100, null= True, blank=True)
    description_project1 = models.TextField(null= True, blank=True)
    reference_project1 = models.CharField(max_length=60,  null= True, blank=True)
    score_project1 = models.FloatField(null= True, blank=True)
    project_goals1 = models.TextField(null= True, blank=True)
    owner_project2 = models.CharField(max_length=100, null= True, blank=True)
    description_project2 = models.TextField(null= True, blank=True)
    reference_project2 = models.CharField(max_length=60, null= True, blank=True)
    score_project2 = models.FloatField(null= True, blank=True)
    project_goals2 = models.TextField(null= True, blank=True)
    cover_image1 = models.URLField(max_length=150)
    cover_image2 = models.URLField(max_length=150)
    last_time = models.DateTimeField(null=True, blank=True)
    total_time = models.FloatField(default=0)
    auth_parent = models.BooleanField(null=True, blank=True)
    
    
    
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
