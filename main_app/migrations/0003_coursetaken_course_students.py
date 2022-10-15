# Generated by Django 4.1.1 on 2022-10-14 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_coursetaught_course_teachers'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTaken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='courses', through='main_app.CourseTaken', to='auth.student'),
        ),
    ]