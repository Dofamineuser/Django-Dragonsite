# Generated by Django 4.0.4 on 2022-05-18 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_author_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.team'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
