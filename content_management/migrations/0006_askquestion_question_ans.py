# Generated by Django 4.2.4 on 2023-08-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0005_askquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='askquestion',
            name='question_ans',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]