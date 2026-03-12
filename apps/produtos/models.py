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

    ORIGEM_CHOICES = [
        ('COMPRA', 'Adquirido (Compras/Almoxarifado)'),
        ('DESENV_PROPRIO', 'Desenvolvimento Fundimar (Engenharia)'),
        ('DESENV_CLIENTE', 'Desenvolvimento sob Encomenda (Exclusivo)'),
    ]

    STATUS_CHOICES = [
        ('PROJETO', 'Em Modelagem/Ferramentaria'),
        ('VIABILIDADE', 'Análise de Mercado'),
        ('ATIVO', 'Liberado para Produção/Venda'),
        ('OBSOLETO', 'Fora de Linha'),
    ]

    codigo_interno = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)

    origem = models.CharField(
        max_length=20, choices=ORIGEM_CHOICES, default='COMPRA')
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='ATIVO')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    responsavel_tecnico = models.ForeignKey(
        'usuarios.User', on_delete=models.SET_NULL, null=True)
    referencia_original = models.CharField(
        max_length=100, blank=True, help_text="Código da montadora original")
    marca_compativel = models.CharField(
        max_length=100, blank=True, help_text="Ex: Compatível com Scania, Volvo")

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
