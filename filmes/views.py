from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import viewsets
from .models import Filme, Ator, Diretor, Conta
from filmes.serializers import DiretorSerializer, AtorSerializer, FilmeSerializer, ContaSerializer


class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class DiretorViewSet(viewsets.ModelViewSet):
    queryset = Diretor.objects.all()
    serializer_class = DiretorSerializer


class AtorViewSet(viewsets.ModelViewSet):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer


@method_decorator(vary_on_cookie)
@method_decorator(cache_page(60*60))
def dispatch(self, *args, **kwargs):
   return super(FilmeViewSet, self).dispatch(*args, **kwargs)
