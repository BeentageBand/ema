# Generated by Django 3.0.6 on 2020-05-25 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('begin_date', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]