# Generated by Django 2.1 on 2018-08-23 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0008_auto_20180823_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatedquestionpaper',
            name='submitted_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
