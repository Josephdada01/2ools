# Generated by Django 5.0.2 on 2024-03-05 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct2lsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('image', models.ImageField(default='', upload_to='images/images')),
            ],
        ),
    ]
