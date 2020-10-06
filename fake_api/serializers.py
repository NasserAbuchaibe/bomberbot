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
                  'selected_course', 'owner_project1', 'description_project1',
                  'reference_project1', 'score_project1', 'project_goals1', 'owner_project2', 'description_project2',
                  'reference_project2', 'score_project2', 'project_goals2', 'cover_image1', 'cover_image2',
                  'last_time', 'total_time', 'auth_parent')
