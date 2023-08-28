# Generated by Django 4.2.3 on 2023-08-28 10:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_candidate_experience_candidate_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='resume',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='smoker',
            field=models.CharField(choices=[('1', 'Yes'), ('2', 'No')], default='2', max_length=50),
        ),
    ]
