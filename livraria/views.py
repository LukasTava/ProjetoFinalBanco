from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import viewsets
from livraria.models import Livro
from livraria.serializer import LivroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class LivrosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os livros"""
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

@api_view(['GET', 'POST'])
def listaLivros(request):
    """"Lista Livros e Cria Novos"""
    if request.method == 'GET':
        data = []
        paginaProx = 1
        paginaAnt = 1
        livros = Livro.objects.all()
        pagina = request.GET.get('page', 1)
        paginator = Paginator(livros, 10)
        try:
            data = paginator.page(pagina)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = LivroSerializer(data, context={'request': request}, many=True)
        if data.has_next():
            paginaProx = data.next_page_number()
        if data.has_previous():
            paginaAnt = data.previous_page_number()

        return Response({'data': serializer.data, 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/customers/?page=' + str(paginaProx), 'prevlink': '/api/customers/?page=' + str(paginaAnt)})
    elif request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def alterarLivro(request, pk):
    """ Imprime, Atualiza e Deleta por ID """
    try:
        customer = Livro.objects.get(pk=pk)
    except Livro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LivroSerializer(customer,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LivroSerializer(customer, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


@method_decorator(vary_on_cookie)
@method_decorator(cache_page(60*60))
def dispatch(self, *args, **kwargs):
   return super(LivroViewSet, self).dispatch(*args, **kwargs)
