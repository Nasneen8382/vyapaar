# Generated by Django 3.2.19 on 2023-12-16 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0007_rename_sale_transaction_saleorder_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesinvoice',
            name='subtotal',
        ),
        migrations.AddField(
            model_name='salesorder',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.party'),
        ),
    ]
