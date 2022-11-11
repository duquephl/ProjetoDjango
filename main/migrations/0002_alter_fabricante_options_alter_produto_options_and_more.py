# Generated by Django 4.1 on 2022-09-26 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fabricante',
            options={'ordering': ['fabricante'], 'verbose_name': 'Fabricante', 'verbose_name_plural': 'Fabricantes'},
        ),
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ['nome_produto'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterField(
            model_name='produto',
            name='fabricante',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.fabricante'),
        ),
    ]