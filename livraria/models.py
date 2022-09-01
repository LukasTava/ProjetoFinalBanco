from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=150)
    editora = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=10)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=1000)
    GENERO = (
        ('R', 'Romance'),
        ('FC', 'Ficção científica'),
        ('D', 'Distopia'),
        ('AA', 'Ação e aventura'),
        ('H', 'Horror'),
        ('FP', 'Ficção Policial'),
        ('B', 'Biografia'),
        ('FH', 'Ficção histórica'),
    )
    genero = models.CharField(max_length=2, choices=GENERO, blank=False, null=False, default='R')

    def __str__(self):
        return self.titulo
