# Generated by Django 3.2.6 on 2021-08-07 00:21

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('qr_gen', '0005_alter_qrfilecode_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrfilecode',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name'),
        ),
    ]
