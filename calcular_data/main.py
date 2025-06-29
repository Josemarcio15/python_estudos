from datetime import datetime
from dateutil.relativedelta import relativedelta


def main():
    hoje = datetime.now().date()
    prixmo_mes = hoje + relativedelta(months=1)
    print(f"hoje{hoje} proximo mes = {prixmo_mes}")
main()


