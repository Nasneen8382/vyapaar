# Generated by Django 3.2.19 on 2023-12-16 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0008_auto_20231216_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesorder',
            name='partyname',
        ),
    ]
