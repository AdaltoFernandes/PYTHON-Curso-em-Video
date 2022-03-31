import math
x = float(input('Digite o ângulo que voce deseja: '))
r = math.radians(x)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)
print('O ângulo de {} tem o SENO de {:.2f}'.format(x, s))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(x, c))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(x, t))

#tentei fazer em uma só linha igual o exemplo e nao deu.
#print('O ângulo tem o SENO de {:.2f}\nO ângulo tem o COSSENO de {:.2f}\nO ângulo  tem a TANGENTE de {:.2f}'.format(s, c, t))