# Generated by Django 2.1.5 on 2019-01-19 18:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0004_entry_entry_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date entered'),
            preserve_default=False,
        ),
    ]
