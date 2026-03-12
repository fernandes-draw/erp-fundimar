import os
import django

# fmt: off
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.produtos.models import Produto, Categoria
# fmt: on

def popular_engenharia():
    print("Cadastrando projetos no Painel de Engenharia...")
    
    # Criar categoria específica se não existir
    cat_pecas, _ = Categoria.objects.get_or_create(nome='Peças de Reposição', setor='Engenharia')
    cat_clientes, _ = Categoria.objects.get_or_create(nome='Projetos Específicos', setor='Clientes')

    projetos = [
        {
            "codigo": "ENG-001", "nome": "Cabeçote Compressor Volvo FH", 
            "origem": "DESENV_PROPRIO", "status": "PROJETO", 
            "marca": "Compatível Volvo", "ref": "VVO-9982"
        },
        {
            "codigo": "ENG-002", "nome": "Cárter de Óleo Scania Euro 6", 
            "origem": "DESENV_PROPRIO", "status": "VIABILIDADE", 
            "marca": "Compatível Scania", "ref": "SCA-1122"
        },
        {
            "codigo": "CLI-990", "nome": "Suporte de Eixo Especial - Ref. 88", 
            "origem": "DESENV_CLIENTE", "status": "PROJETO", 
            "cliente": "Scania Brasil"
        },
        {
            "codigo": "ENG-005", "nome": "Polia de Transmissão Industrial", 
            "origem": "DESENV_PROPRIO", "status": "ATIVO", 
            "marca": "Linha Própria Fundimar"
        },
    ]

    for p in projetos:
        Produto.objects.update_or_create(
            codigo_interno=p['codigo'],
            defaults={
                'nome': p['nome'],
                'tipo': 'PA', # Produto Acabado
                'categoria': cat_pecas if 'ENG' in p['codigo'] else cat_clientes,
                'origem': p['origem'],
                'status': p['status'],
                'marca_compativel': p.get('marca', ''),
                'referencia_original': p.get('ref', ''),
                'cliente_exclusivo': p.get('cliente', None),
                'unidade_medida': 'un'
            }
        )
    
    print("Projetos de engenharia inseridos com sucesso!")

if __name__ == '__main__':
    popular_engenharia()