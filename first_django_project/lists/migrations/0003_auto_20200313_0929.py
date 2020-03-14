# Generated by Django 3.0.3 on 2020-03-13 09:29

from django.db import migrations, models
import lists.models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.TextField(default=None, verbose_name=lists.models.List),
        ),
    ]
