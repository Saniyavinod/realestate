# Generated by Django 5.1.3 on 2024-11-09 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('property_type', models.CharField(choices=[('apartment', 'Apartment'), ('house', 'House'), ('land', 'Land'), ('villa', 'Villa'), ('commercial', 'Commercial')], max_length=50)),
                ('number_of_bedrooms', models.PositiveIntegerField()),
                ('square_footage', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=100)),
                ('property_image', models.ImageField(blank=True, null=True, upload_to='properties/')),
                ('contact_details', models.CharField(max_length=255)),
            ],
        ),
    ]