# apps/dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required  # Isso garante que só logados acessem
def index(request):
    return render(request, 'dashboard/index.html')
