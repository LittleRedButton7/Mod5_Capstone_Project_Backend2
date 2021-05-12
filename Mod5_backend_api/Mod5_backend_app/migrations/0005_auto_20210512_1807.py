# Generated by Django 3.2.2 on 2021-05-12 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mod5_backend_app', '0004_auto_20210512_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='calories',
            field=models.CharField(default=0, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='carbs',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='protein',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
