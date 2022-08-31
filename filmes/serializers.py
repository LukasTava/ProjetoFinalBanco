from rest_framework import serializers
from .models import Ator, Diretor, Filme, Conta


class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ('id','titulo', 'ano', 'genero', 'sinopse', 'imagem')


class AtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ator
        fields = '__all__'


class DiretorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diretor
        fields = '__all__'

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = '__all__'
