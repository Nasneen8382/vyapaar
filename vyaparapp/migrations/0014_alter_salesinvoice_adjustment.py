# Generated by Django 3.2.19 on 2023-12-22 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0013_alter_salesinvoice_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesinvoice',
            name='adjustment',
            field=models.CharField(default=0, max_length=100, null=True),
        ),
    ]
