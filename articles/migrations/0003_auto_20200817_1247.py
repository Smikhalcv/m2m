# Generated by Django 2.2.10 on 2020-08-17 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tegs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tegs',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]