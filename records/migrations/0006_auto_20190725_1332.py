# Generated by Django 2.2.3 on 2019-07-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_auto_20190725_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='be_program_type',
            field=models.CharField(blank=True, choices=[('Regular', 'Regular'), ('Full Fee', 'Full Fee')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='msc_program_type',
            field=models.CharField(blank=True, choices=[('Regular', 'Regular'), ('Full Fee', 'Full Fee')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phd_program_type',
            field=models.CharField(blank=True, choices=[('Regular', 'Regular'), ('Full Fee', 'Full Fee')], max_length=10, null=True),
        ),
    ]
