# Generated by Django 5.1.3 on 2024-11-17 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, null=True, verbose_name='product title')),
                ('title_fa', models.CharField(max_length=127, null=True, verbose_name='product title')),
                ('title_en', models.CharField(max_length=127, null=True, verbose_name='product title')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='product price')),
            ],
        ),
    ]
