#import random
from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
#escolhido = random.choice(lista)
escolhido = choice(lista)
print('O aluno escolhi foi {}'.format(escolhido))
