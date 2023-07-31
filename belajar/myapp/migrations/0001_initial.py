# Generated by Django 4.2.3 on 2023-07-31 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(choices=[('ACT', 'Action'), ('DRM', 'Drama'), ('COM', 'Comedy')], max_length=3)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
