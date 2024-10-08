# Generated by Django 4.1.4 on 2022-12-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(default='CEC tasty items', max_length=40)),
                ('image', models.ImageField(upload_to='items')),
                ('prize', models.PositiveSmallIntegerField()),
                ('categoryID', models.PositiveSmallIntegerField()),
                ('rating', models.FloatField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
