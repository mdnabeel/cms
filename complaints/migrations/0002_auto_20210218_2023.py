# Generated by Django 3.1.6 on 2021-02-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faultdetail',
            name='date_of_rectification',
            field=models.DateField(blank=True, null=True),
        ),
    ]
