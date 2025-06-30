from datetime import datetime, date
from dateutil.relativedelta import relativedelta


def primeira_mensalidade(dia_do_pagamento):

    hoje = date(2025,2,25)
    print(f"hoje é {hoje}")

    vencimento_corrigido = hoje + relativedelta(months=1, day=dia_do_pagamento)

    print(f"mudanca de data: {vencimento_corrigido}")
    dias_a_pagar = (vencimento_corrigido - hoje).days
    print(f"voce tem que pagar {dias_a_pagar} dias")


primeira_mensalidade(31)