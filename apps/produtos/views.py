from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Produto


@login_required
def produto_list(request):
    produtos = Produto.objects.all().select_related('categoria')
    return render(request, 'produtos/produto_list.html', {'produtos': produtos})
