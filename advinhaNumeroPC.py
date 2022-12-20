#Jogo simples de advinhar contra o computador

import random

def advinha(x):
    random_number = random.randint(1,x)
    chute = 0
    erros = 0
    while chute != random_number:
        
        chute = int(input(f"Advinhe o número entre 1 e {x}: "))

        if chute > random_number:
            erros = erros +1
            print(f"Você chutou um número MAIOR do que o número pensei!\n ERROS = {erros}")
            
        elif chute < random_number:
            erros = erros +1
            print(f"Você chutou um número MENOR do que o número pensei!\n ERROS = {erros}")
        else:
            break
        if erros >= 3:
            print("Você perdeu!")
            exit()
            return(0)
    
    print(f"Você advinhou certo! O número era {random_number}")


print("################## Bem vindo ao jogo de Advinhação ##################\n\
Irei pensar num número e você precisa advinhar. \n\
Se errar 3 vezes você perde. Pronto?")

max = int(input("Digite o maior número que será usado no jogo de advinhação: "))
advinha(max)

