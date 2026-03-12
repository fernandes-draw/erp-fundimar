from django.shortcuts import render

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
