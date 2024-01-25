# FREEDONIA

from decimal import Decimal


percentuais = {
    'Chico': Decimal('0.5'),
    'Groucho': Decimal('0.7'),
    'Harpo': Decimal('0.5'),
    'Zeppo': Decimal('0.4')
    }

def percentual_hora(hora):
    return hora / Decimal('24.0')

def calcular_imposto(total, estado, hora):
    
    class HoraEhMuitoBaixaErro(Exception): pass
    class HoraEhMuitoAltaErro(Exception): pass
    
    if hora < 0:
        raise HoraEhMuitoBaixaErro(f'Hora {hora} é < 0')
    if hora >= 24:
        raise HoraEhMuitoAltaErro(f'Hora {hora} é >= 24')
    return float(total + (total * percentuais[estado] * percentual_hora(hora)))

