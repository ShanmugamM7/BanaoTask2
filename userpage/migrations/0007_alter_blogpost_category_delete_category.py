# Generated by Django 4.2.9 on 2024-02-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0006_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('Mental Health', 'Mental Health'), ('Heart Disease', 'Heart Disease'), ('Covid19', 'Covid19'), ('Immunization', 'Immunization')], default='', max_length=32),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
