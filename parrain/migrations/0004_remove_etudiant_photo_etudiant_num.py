# Generated by Django 4.0 on 2022-01-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parrain', '0003_alter_parrainage_matfilleul_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='photo',
        ),
        migrations.AddField(
            model_name='etudiant',
            name='num',
            field=models.IntegerField(blank=True, max_length=7, null=True),
        ),
    ]
