class Banks:
    ITAU = 341


class RegistrationType:
    PESSOA_FISICA = "1"
    PESSOA_JURIDICA = "2"


class Segment:
    "Pagamento Através de Crédito em Conta, Cheque,OP, DOC, TED ou Pagamento com Autenticação"
    PAGAMENTO_CREDITO_CONTA_TED_DOC_CHEQUE = "A"

    "Pagamento de Títulos de Cobrança"
    PAGAMENTO_TITULOS_DE_COBRANCA = "J"
    PAGAMENTO_TITULOS_DE_COBRANCA_J52 = "J52"

    "Pagamento de Contas e Tributos com Código de Barras (Obrigatório - Remessa / Retorno)"
    PAGAMENTO_CONTAS_TRIBUTOS_COM_CODIGO_DE_BARRAS = "O"


class ServiceType:      # P005

    CREDITO_EM_CONTA = "01"
    PAGAMENTO_DE_ALUGUEL_CONDOMINIO = "02"

    # "03" = Pagamento de Duplicata/Títulos
    # "04" = Pagamento de Dividendos
    # "05" = Pagamento de Mensalidade Escolar
    # "06" = Pagamento de Salários
    # "07" = Pagamento a Fornecedores
    # "08" = Operações de Câmbios/Fundos/Bolsa de Valores
    # "09" = Repasse de Arrecadação/Pagamento de Tributos
    # "10" = Transferência Internacional em Real
    # "11" = DOC para Poupança
    # "12" = DOC para Depósito Judicial
    # "13" = Outros
    # "16" = Pagamento de bolsa auxílio
    # "17" = Remuneração à cooperado
    # "18" = Pagamento de honorários
    # "19" = Pagamento de prebenda (Remuneração a padres e sacerdotes)


class HeaderLoteServiceType:    # G025
    
    COBRANCA = "01"
    BOLETO_DE_PAMENTO_ELETRONICO = "03"
    CONCILIACAO_BANCARIA = "04"
    DEBITOS = "05"
    CUSTODIA_DE_CHEQUES = "06"
    GESTAO_DE_CAIXA = "07"
    CONSULTA_INFORMACAO_MARGEM = "08"
    PAGAMENTOS_DIVERSOS = "98"
    # Averbação da Consignação/Retenção = "09"
    # Pagamento Dividendos = "10"
    # Manutenção da Consignação = "11"
    # Consignação de Parcelas = "12"
    # Glosa da Consignação (INSS) = "13"
    # Consulta de Tributos a pagar = "14"
    PAGAMENTO_FORNECEDOR = "20"
    # Pagamento de Contas, Tributos e Impostos = "22"
    # Interoperabilidade entre Contas de Instituições de Pagamentos = "23"
    # Compror = "25"
    # Compror Rotativo = "26"
    # Alegação do Pagador = "29"
    # Pagamento Salários = "30"
    # Pagamento de honorários = "32"
    # Pagamento de bolsa auxílio = "33"
    # Pagamento de prebenda (remuneração a padres e sacerdotes) = "34"
    # Vendor = "40"
    # Vendor a Termo = "41"
    # Pagamento Sinistros Segurados = "50"
    # Pagamento Despesas Viajante em Trânsito = "60"
    # Pagamento Autorizado = "70"
    # Pagamento Credenciados = "75"
    # Pagamento de Remuneração = "77"
    # Pagamento Representantes / Vendedores Autorizados = "80"
    # Pagamento Benefícios = "90"


class HeaderLoteEntryWay:    # G029
    """
    Forma de Lançamento
    """
    CREDITO_EM_CONTA_CORRENTE_SALARIO = "01"
    TED_OUTRA_TITULARIDADE = "41"
    TED_MESMA_TITULARIDADE = "43"
    LIQUIDACAO_TITULOS_PROPRIO_BANCO = "30"
    PAGAMENTO_DE_TITULOS_DE_OUTROS_BANCOS = "31"

    """
    
    "02" = Cheque Pagamento / Administrativo
    "03" = DOC/TED (1) (2)
    "04" = Cartão Salário (somente para Tipo de Serviço = "30")
    "05" = Crédito em Conta Poupança
    "10" = OP à Disposição
    "11" = Pagamento de Contas e Tributos com Código de Barras
    "16" = Tributo - DARF Normal
    "17" = Tributo - GPS (Guia da Previdência Social)
    "18" = Tributo - DARF Simples
    "19" = Tributo - IPTU – Prefeituras
    "20" = Pagamento com Autenticação
    "21" = Tributo – DARJ
    "22" = Tributo - GARE-SP ICMS
    "23" = Tributo - GARE-SP DR
    "24" = Tributo - GARE-SP ITCMD
    "25" = Tributo - IPVA
    "26" = Tributo - Licenciamento
    "27" = Tributo – DPVAT
    "40" = Extrato de Conta Corrente
    
    "44" = TED para Transferência de Conta Investimento
    "50" = Débito em Conta Corrente
    "70" = Extrato para Gestão de Caixa
    "71" = Depósito Judicial em Conta Corrente
    "72" = Depósito Judicial em Poupança
    "73" = Extrato de Conta Investimento
    "80"= Pagamento de tributos municipais ISS – LCP 157 – próprio Banco
    "81"= Pagamento de Tributos Municipais ISS – LCP 157 – outros Bancos
    """