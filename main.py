import os

def multa_localidade(velocidade):
    if velocidade <= 50:
        return 0
    elif velocidade > 50:
        return 60
    elif velocidade >= 90:
        return 120
    elif velocidade >= 120:
        return 320
    
def multa_fora_localidade(velocidade):
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
    
def calcular_multa(velocidade, loc):
    if loc == 1:
        return multa_localidade(velocidade)
    elif loc == 2:
        return multa_fora_localidade(velocidade)
    elif loc == 3:
        return multa_autoestrada(velocidade)
    else:
        print("Opção inválida!")
        return None
    
def main():
    print("--------- Bem-vindo ao Sistema de Multas ---------")
    try:
       velocidade = float(input("Registe a velocidade do automóvel ligeiro: ")) 