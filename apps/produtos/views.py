from django.shortcuts import render, get_object_or_404
from .models import Produto

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Produto


@login_required
def produto_list(request):
    setor = request.GET.get('setor')
    produtos = Produto.objects.all().select_related('categoria')

    if setor == 'suprimentos':
        # Filtra apenas o que é comprado para a fundição/manutenção
        produtos = produtos.filter(origem='COMPRA')
    elif setor == 'engenharia':
        # Filtra o que é desenvolvido pela Fundimar ou para Clientes
        produtos = produtos.exclude(origem='COMPRA')

    return render(request, 'produtos/produto_list.html', {'produtos': produtos, 'setor': setor})

def produto_detail(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    # A variável global do sistema conforme solicitado
    NOME_SISTEMA = "ERP FUNDIMAR - GESTÃO INDUSTRIAL" 
    
    return render(request, 'produtos/produto_detail.html', {
        'produto': produto,
        'nome_sistema': NOME_SISTEMA
    })