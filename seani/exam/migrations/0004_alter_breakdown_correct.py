# Generated by Django 5.0.2 on 2024-03-06 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_alter_exam_options_exam_created_exam_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakdown',
            name='correct',
            field=models.CharField(default='-', max_length=5, verbose_name='Correcta'),
        ),
    ]
