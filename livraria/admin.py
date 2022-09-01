from django.contrib import admin
from livraria.models import Livro


class Livros(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'editora', 'ISBN', 'valor', 'descricao', 'genero')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20


admin.site.register(Livro, Livros)
