# Generated by Django 4.0.1 on 2023-09-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_preferences_userinteraction'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]