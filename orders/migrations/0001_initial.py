# Generated by Django 4.1.5 on 2023-01-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=10)),
                ('product_id', models.PositiveSmallIntegerField()),
                ('order_id', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField()),
                ('date_delivary', models.DateTimeField()),
                ('total_prize', models.PositiveSmallIntegerField()),
                ('quantity', models.PositiveSmallIntegerField()),
            ],
        ),
    ]