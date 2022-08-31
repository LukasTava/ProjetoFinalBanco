from django.db import models


class Filme(models.Model):
    id = models.AutoField(auto_created = True, primary_key = True),
    titulo = models.CharField(max_length=100)
    ano = models.DecimalField(max_digits=4, decimal_places=0)
    sinopse = models.TextField(max_length=1000)
    GENERO = (
        ('R', 'Romance'),
        ('FC', 'Ficção científica'),
        ('D', 'Distopia'),
        ('AA', 'Ação e aventura'),
        ('H', 'Horror'),
        ('FP', 'Ficção Policial'),
        ('B', 'Biografia'),
        ('FH', 'Ficção histórica'),
        ('DC', 'Documentário'),
        ('DR', 'Drama'),
        ('SP', 'Super Herói')
    )
    genero = models.CharField(max_length=2, choices=GENERO, blank=False, null=False, default='AA')
    imagem = models.ImageField(default=None)

    def __str__(self):
        return self.titulo

class Ator(models.Model):
    nome = models.CharField(max_length=100)
    filme = models.ManyToManyField(Filme)

    def __str__(self):
        return self.nome

class Diretor(models.Model):
    nome = models.CharField(max_length=100)
    filme = models.ManyToManyField(Filme)

    def __str__(self):
        return self.nome

class Conta(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    dataNasc = models.DateField
    assistido = models.ManyToManyField(Filme)

    def __str__(self):
        return self.nome

