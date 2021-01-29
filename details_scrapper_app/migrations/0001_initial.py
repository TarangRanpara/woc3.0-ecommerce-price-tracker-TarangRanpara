# Generated by Django 3.1.5 on 2021-01-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=1000)),
                ('site', models.CharField(max_length=2)),
                ('price', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
