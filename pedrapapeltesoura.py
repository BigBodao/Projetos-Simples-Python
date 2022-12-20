#Jogo simples de pedra papel tesoura

    #r: pedra   -   p: papel  -   t:tesoura
    #r>t    |   p>r |   t>p

import random

def jogo():
    jogador = input("Digite 'r' para Pedra. 'p' para Papel. 't' para Tesoura.\n")
    computador = random.choice(['r','p','t'])

    if jogador == computador:
        return 'empate'
    if vitoria(jogador, computador):
        return 'vitória'
    return 'derrota'

def vitoria (jogador, oponente):
    if (jogador == 'r' and oponente =='t') or \
        (jogador == 'p' and oponente == 'r') or \
        (jogador == 't' and oponente == 'p'):
        return True

print(jogo())