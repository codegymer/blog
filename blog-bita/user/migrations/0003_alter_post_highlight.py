# Generated by Django 4.0.4 on 2022-06-04 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_post_highlight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='highlight',
            field=models.CharField(default='Highlight Not Provided!', max_length=1000, null=True),
        ),
    ]
