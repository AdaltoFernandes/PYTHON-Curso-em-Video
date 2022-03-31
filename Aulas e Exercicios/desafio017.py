import math
co = float(input('Diga o comprimento do cateto oposto: '))
ca = float(input('Diga o comprimento do cateto adjacente: '))
hipo = math.hypot(co, ca)
print('O comprimento da hipotenusa é de: {} '.format(hipo))
