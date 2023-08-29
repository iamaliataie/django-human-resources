# Generated by Django 4.2.3 on 2023-08-29 05:30

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_candidate_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='databases',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Mysql', 'Mysql'), ('Posgresql', 'Posgresql'), ('Mangodb', 'Mangodb'), ('Sqlite3', 'Sqlite3'), ('Oracle', 'Oracle'), ('Other', 'Other')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='candidate',
            name='frameworks',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('React', 'React'), ('Vue', 'Vue'), ('Django', 'Django'), ('Laravel', 'Laravel'), ('RubyOnRails', 'RubyOnRails'), ('Other', 'Other')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='candidate',
            name='libraries',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Jquery', 'Jquery'), ('Chart.js', 'Chart.js'), ('Gsap', 'Gsap'), ('Graphql', 'Graphql'), ('Matplotlib', 'Matplotlib'), ('Other', 'Other')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='candidate',
            name='mobile',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('React Native', 'React Native'), ('Kivy', 'Kivy'), ('Flutter', 'Flutter'), ('Ionic', 'Ionic'), ('Xamarin', 'Xamarin'), ('Other', 'Other')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='candidate',
            name='other',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('UML', 'UML'), ('SQL', 'SQL'), ('Docker', 'Docker'), ('GIT', 'GIT'), ('Pandas', 'Pandas'), ('Other', 'Other')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Python', 'Python'), ('Javascript', 'Javascript'), ('C++', 'C++'), ('PHP', 'PHP'), ('Ruby', 'Ruby'), ('Other', 'Other')], default='', max_length=20),
        ),
    ]
