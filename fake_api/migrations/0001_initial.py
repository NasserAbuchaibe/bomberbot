# Generated by Django 3.1.2 on 2020-10-06 18:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParentsModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firts_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firts_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('teacher', models.CharField(max_length=100)),
                ('classroom_id', models.CharField(max_length=60, unique=True)),
                ('access_code', models.CharField(max_length=60)),
                ('selected_course', models.CharField(max_length=60)),
                ('owner_project', models.CharField(max_length=100)),
                ('description_project', models.TextField()),
                ('reference_project', models.CharField(max_length=60)),
                ('cover_image1', models.URLField(max_length=150)),
                ('cover_image2', models.URLField(max_length=150)),
                ('last_time', models.DateTimeField(blank=True, null=True)),
                ('total_time', models.FloatField(default=0)),
                ('parent', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fake_api.parentsmodel')),
            ],
            options={
                'ordering': ['username'],
            },
        ),
    ]