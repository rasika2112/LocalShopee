# Generated by Django 3.0.2 on 2020-05-31 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_cinfo_aadhar'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinfo',
            name='Confirm',
            field=models.CharField(default='abcd', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vinfo',
            name='Confirm',
            field=models.CharField(default='abcd', max_length=20),
            preserve_default=False,
        ),
    ]
