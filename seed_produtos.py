from apps.produtos.models import Produto, Categoria
import os
import django

# Configuração do ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()


def popular_banco():
    print("Iniciando a população de dados para Fundimar...")

    # 1. Criar Categorias
    cat_mp, _ = Categoria.objects.get_or_create(
        nome='Ligas e Metais', setor='Fundição')
    cat_ins, _ = Categoria.objects.get_or_create(
        nome='Insumos Químicos', setor='Fundição')
    cat_pa, _ = Categoria.objects.get_or_create(
        nome='Peças Automotivas', setor='Produção')
    cat_man, _ = Categoria.objects.get_or_create(
        nome='Materiais Elétricos', setor='Manutenção')
    cat_fer, _ = Categoria.objects.get_or_create(
        nome='Ferramentas de Corte', setor='Ferramentaria')

    # 2. Criar Produtos de exemplo
    produtos_data = [
        {
            "codigo_interno": "MP-001", "nome": "Ferro Gusa LD", "tipo": "MP",
            "categoria": cat_mp, "unidade": "tn", "estoque": 25.5, "min": 10.0
        },
        {
            "codigo_interno": "MP-002", "nome": "Ferro Manganês HC", "tipo": "MP",
            "categoria": cat_mp, "unidade": "kg", "estoque": 450, "min": 500  # Alerta estoque baixo
        },
        {
            "codigo_interno": "IN-010", "nome": "Resina Fenólica", "tipo": "IN",
            "categoria": cat_ins, "unidade": "kg", "estoque": 1200, "min": 200
        },
        {
            "codigo_interno": "PA-501", "nome": "Bloco de Motor V8", "tipo": "PA",
            "categoria": cat_pa, "unidade": "un", "estoque": 42, "min": 10, "cliente": "Scania Brasil"
        },
        {
            "codigo_interno": "FE-005", "nome": "Fresa de Topo Metal Duro 12mm", "tipo": "FE",
            "categoria": cat_fer, "unidade": "un", "estoque": 5, "min": 2
        },
        {
            "codigo_interno": "MN-088", "nome": "Cabo Flexível 2.5mm", "tipo": "MN",
            "categoria": cat_man, "unidade": "mt", "estoque": 100, "min": 20
        },
    ]

    for p in produtos_data:
        Produto.objects.update_or_create(
            codigo_interno=p['codigo_interno'],
            defaults={
                'nome': p['nome'],
                'tipo': p['tipo'],
                'categoria': p['categoria'],
                'unidade_medida': p['unidade'],
                'estoque_atual': p['estoque'],
                'estoque_minimo': p['min'],
                'cliente_exclusivo': p.get('cliente', None)
            }
        )

    print("Dados inseridos com sucesso!")


if __name__ == '__main__':
    popular_banco()
