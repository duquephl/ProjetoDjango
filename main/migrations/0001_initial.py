# Generated by Django 4.1 on 2022-09-11 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricante', models.CharField(max_length=100)),
                ('imagem_logo', models.ImageField(upload_to='images/fabricantes/')),
                ('sobre', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=256)),
                ('codigo_de_barra', models.PositiveBigIntegerField()),
                ('preco', models.FloatField()),
                ('gramatura', models.FloatField()),
                ('imagem_produto', models.ImageField(upload_to='images/produtos/')),
                ('sobre', models.TextField()),
                ('fabricante', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='main.fabricante')),
            ],
        ),
    ]
