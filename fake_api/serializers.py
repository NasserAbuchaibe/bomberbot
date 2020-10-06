from rest_framework import serializers
from .models import ParentsModel, StudentModel
# Convert the querysets of the models in JSON
# to serve them in the REST API

class ParentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParentsModel
        fields = ('id',)

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentModel
        fields = ('id', 'firts_name', 'last_name', 'username',
                  'password', 'teacher', 'classroom_id', 'access_code',
                  'selected_course', 'owner_project', 'description_project',
                  'reference_project', 'cover_image1', 'cover_image2',
                  'last_time', 'total_time')
