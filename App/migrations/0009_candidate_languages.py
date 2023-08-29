# Generated by Django 4.2.3 on 2023-08-29 05:28

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_candidate_resume_alter_candidate_smoker'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Python', 'Python'), ('Javascript', 'Javascript'), ('C++', 'C++'), ('PHP', 'PHP'), ('Ruby', 'Ruby'), ('Other', 'Other')], default='', max_length=100),
        ),
    ]
