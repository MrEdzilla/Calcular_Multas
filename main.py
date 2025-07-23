import os

velocidade = float(input("Registe a velocidade do automóvel ligeiro: "))
tipo_via = input("Registe o tipo de via em que circulava (localidade / fora / autoestrada)").strip().lower()

def multa_localidade(velocidade):
    if velocidade <= 50:
        return 0
    elif velocidade > 50:
        return 60
    elif velocidade >= 90:
        return 120
    elif velocidade >= 120:
        return 320
    
def multa_fora(velocidade):
    if velocidade <= 90:
        return 0
    elif velocidade > 90:
        return 60
    elif velocidade >= 120:
        return 120

def multa_autoestrada(velocidade):
    if velocidade <= 120:
        return 0
    elif velocidade > 120:
        return 60
    elif velocidade >= 150:
        return 120
    elif velocidade >= 175:
        return 360