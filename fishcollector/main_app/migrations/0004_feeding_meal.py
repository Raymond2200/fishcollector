# Generated by Django 3.1.7 on 2021-03-31 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210331_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeding',
            name='meal',
            field=models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1, verbose_name='meals'),
        ),
    ]
