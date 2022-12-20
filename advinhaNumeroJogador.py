#Jogo simples de advinhar contra outro jogador
import random

def advinhar(x):
    chute = 0
    tentativas = []
    erros = 0
    dica1 = str(x)
    print(f"DICA: O número a ser advinhado tem: {len(dica1)} digitos")

    while chute != x:
        print(f"Suas tentativas até agora: {tentativas}")
        chute = int(input(f"Jogador 2, tente advinhar o número do Jogador 1: "))
        tentativas.append(chute)
        
        if chute > x:
            print(f"Você errou. O número que você chutou é MAIOR.")
            erros = erros +1
        elif chute < x:
            print(f"Você errou. O número que você chutou é MENOR.")
            erros = erros +1
        else:
            break
        
        if erros >= 3:
            print(f"JOGADOR 1 GANHOU! O número certo era: {x}")
            exit()

    print(f'JOGADOR 2 GANHOU!, você advinhou o número!')

print("BEM VINDO AO JOGO DA ADVINHAÇÃO\n\
Jogador 1, digite um número qualquer.\n\
Jogador 2, tente advinhar!")
numero = int(input(f"Jogador 1, insira o número: "))

advinhar(numero)