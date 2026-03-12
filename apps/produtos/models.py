from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    # Ex: Fundição, Escritório, Manutenção
    setor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.setor} - {self.nome}"


class Produto(models.Model):
    # Escolhas fixas para lógica de sistema
    TIPO_CHOICES = [
        ('MP', 'Matéria-Prima'),       # Gusa, Ferro, Ligas
        ('IN', 'Insumo/Consumível'),  # Areia, Resina, Filtros
        ('PA', 'Produto Acabado'),    # Peça final do cliente
        ('MN', 'Manutenção/Uso Geral'),  # Limpeza, Elétrica
        ('FE', 'Ferramentaria'),      # Blocos de aço, Ferramentas de usinagem
    ]

    codigo_interno = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)

    # Unidade de Medida (Crucial para fundição: kg, tn, un, par)
    unidade_medida = models.CharField(max_length=10, default='kg')

    # Especificidade para Produtos de Clientes (Peças Acabadas)
    cliente_exclusivo = models.CharField(max_length=100, blank=True, null=True,
                                         help_text="Se preenchido, este produto só pertence a este cliente.")

    # Controle de Estoque
    estoque_minimo = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    estoque_atual = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    # Custos (Opcional agora, mas vital depois)
    preco_custo = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"[{self.codigo_interno}] {self.nome}"
