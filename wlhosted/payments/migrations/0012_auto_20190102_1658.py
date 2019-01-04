# Generated by Django 2.1.4 on 2019-01-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0011_payment_amount_fixed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='recurring',
            field=models.CharField(blank=True, choices=[('y', 'Annual'), ('b', 'Biannual'), ('m', 'Monthly'), ('', 'Onetime')], default='', max_length=10),
        ),
    ]