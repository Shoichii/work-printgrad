# Generated by Django 4.2 on 2024-01-14 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_alter_candidate_resume_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='resume_file',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Резюме'),
        ),
    ]