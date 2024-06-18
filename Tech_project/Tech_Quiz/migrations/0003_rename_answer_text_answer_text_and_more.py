# Generated by Django 5.0.6 on 2024-06-12 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tech_Quiz', '0002_answer_is_correct_option_is_correct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='option',
            old_name='option_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='Tech_Quiz.question'),
        ),
    ]
