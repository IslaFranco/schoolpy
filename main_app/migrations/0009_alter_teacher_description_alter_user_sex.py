# Generated by Django 4.1.1 on 2022-10-07 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_remove_teacherprofile_user_delete_studentprofile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=10),
        ),
    ]