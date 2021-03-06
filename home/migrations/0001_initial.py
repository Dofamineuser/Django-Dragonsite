# Generated by Django 4.0.4 on 2022-05-16 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('facebook', models.CharField(default='#', max_length=100)),
                ('instagram', models.CharField(default='#', max_length=100)),
                ('twitter', models.CharField(default='#', max_length=100)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
