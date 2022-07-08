# Generated by Django 4.0.4 on 2022-07-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20220706_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.CharField(choices=[('Ağ', 'Ağ'), ('Qara', 'Qara'), ('Mavi', 'Mavi'), ('Qırmızı', 'Qırmızı'), ('Sarı', 'Sarı'), ('Bənövşəyi', 'Bənövşəyi'), ('Digər', 'Digər')], max_length=50),
        ),
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.CharField(choices=[('X', 'X'), ('M', 'M'), ('XL', 'XL'), ('Yoxdur', 'Yoxdur')], max_length=50),
        ),
    ]