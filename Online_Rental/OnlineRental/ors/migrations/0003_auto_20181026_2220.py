# Generated by Django 2.1.2 on 2018-10-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ors', '0002_auto_20181026_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistory',
            name='dateEnd',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='dateStart',
            field=models.DateField(null=True),
        ),
    ]
