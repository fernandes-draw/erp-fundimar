from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.setor} - {self.nome}"

class Produto(models.Model):
    TIPO_CHOICES = [
        ('MP', 'Matéria-Prima'),
        ('IN', 'Insumo/Consumível'),
        ('PA', 'Produto Acabado'),
        ('MN', 'Manutenção/Uso Geral'),
        ('FE', 'Ferramentaria'),
    ]

    ORIGEM_CHOICES = [
        ('COMPRA', 'Adquirido (Compras/Almoxarifado)'),
        ('DESENV_PROPRIO', 'Desenvolvimento Fundimar (Engenharia)'),
        ('DESENV_CLIENTE', 'Desenvolvimento sob Encomenda (Exclusivo)'),
    ]

    # Status focado no CICLO DE VIDA DO PROJETO (Engenharia)
    STATUS_PROJETO_CHOICES = [
        ('VIABILIDADE', 'Análise de Mercado'),
        ('PROJETO', 'Em Modelagem (CAD)'),
        ('FERRAMENTARIA', 'Em Produção (Ferramentaria/CNC)'),
        ('CONCLUIDO', 'Projeto Concluído'),
        ('OBSOLETO', 'Fora de Linha'),
    ]

    # Estágios da PRODUÇÃO REAL (Chão de Fábrica)
    ESTAGIO_PRODUCAO_CHOICES = [
        ('AGUARDANDO', 'Aguardando Início'),
        ('MOLDAGEM', 'Moldagem'),
        ('CURA', 'Cura'),
        ('ENVAZE', 'Envaze'),
        ('RESFRIAMENTO', 'Resfriamento'),
        ('QUEBRA_CANAL', 'Quebra de Canal'),
        ('REBARBACAO', 'Rebarbação'),
        ('JATEAMENTO', 'Jateamento'),
        ('CONTAGEM', 'Contagem/Inspeção'),
        ('ESTOQUE', 'Disponível em Estoque'),
    ]

    LINHA_CHOICES = [
        ('AUTOMOTIVA', 'Linha Automotiva (Pesada)'),
        ('AGRICOLA', 'Linha Agrícola'),
        ('OUTROS', 'Outros'),
    ]

    # Identificação
    codigo_interno = models.CharField(max_length=50, unique=True, verbose_name="REF. MODEL")
    nome = models.CharField(max_length=200, verbose_name="Descrição")
    linha = models.CharField(max_length=20, choices=LINHA_CHOICES, default='AUTOMOTIVA')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, default='PA')

    # Detalhes Técnicos
    material_peca = models.CharField(max_length=50, blank=True, verbose_name="Material Peça")
    material_ferramental = models.CharField(max_length=50, blank=True, verbose_name="Material Ferram.")
    peso_bruto_amostra = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    figuras_por_caixa = models.IntegerField(default=1)
    quantidade_caixa_macho = models.CharField(max_length=50, blank=True)

    # Controle e Arquivos
    caminho_projeto_cad = models.CharField(max_length=500, blank=True)
    ficha_processo = models.CharField(max_length=200, blank=True)
    observacoes_tecnicas = models.TextField(blank=True)
    
    # Status Dinâmicos
    origem = models.CharField(max_length=20, choices=ORIGEM_CHOICES, default='DESENV_PROPRIO')
    status_projeto = models.CharField(max_length=20, choices=STATUS_PROJETO_CHOICES, default='PROJETO')
    estagio_producao = models.CharField(max_length=20, choices=ESTAGIO_PRODUCAO_CHOICES, default='AGUARDANDO')
    
    data_cadastro = models.DateField(auto_now_add=True)
    data_ultima_alteracao = models.DateField(auto_now=True)
    
    # Administrativo
    cliente_exclusivo = models.CharField(max_length=100, blank=True, null=True)
    unidade_medida = models.CharField(max_length=10, default='un')
    estoque_minimo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estoque_atual = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"[{self.codigo_interno}] {self.nome}"