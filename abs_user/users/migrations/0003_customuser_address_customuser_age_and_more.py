# Generated by Django 4.1.4 on 2022-12-24 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_customuser_address_remove_customuser_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='public_visibility',
            field=models.BooleanField(default=False),
        ),
    ]
