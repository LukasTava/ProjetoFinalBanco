# Generated by Django 4.1 on 2022-08-30 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=150)),
                ('editora', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=10)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=3)),
                ('descricao', models.CharField(max_length=1000)),
                ('genero', models.CharField(choices=[('R', 'Romance'), ('FC', 'Ficção científica'), ('D', 'Distopia'), ('AA', 'Ação e aventura'), ('H', 'Horror'), ('FP', 'Ficção Policial'), ('B', 'Biografia'), ('FH', 'Ficção histórica')], default='R', max_length=2)),
            ],
        ),
    ]