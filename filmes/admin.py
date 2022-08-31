from django.contrib import admin
from .models import Filme, Diretor, Ator, Conta


class Filmes(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'ano', 'sinopse', 'genero')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)


admin.site.register(Filme, Filmes)


class Diretores(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Diretor, Diretores)


class Atores(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Ator, Atores)


class Contas(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Conta, Contas)