# Generated by Django 3.0.3 on 2020-07-02 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0003_advertising_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertising',
            old_name='page_size',
            new_name='banner_size',
        ),
        migrations.RenameField(
            model_name='advertisinginfo',
            old_name='page_size',
            new_name='banner_size',
        ),
    ]