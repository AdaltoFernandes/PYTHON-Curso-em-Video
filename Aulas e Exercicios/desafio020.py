import random
#from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
#mais resumido com o from random import, colocando: shuffle(lista)
print('A ordem de apresentação será \n{}'.format(lista))