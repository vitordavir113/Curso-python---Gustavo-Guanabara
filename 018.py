from math import radians
from math import sin
from math import tan
from math import cos
ang = int(input('Digite o angulo para extrair o seno cosseno e a tangente'))
rad = radians(ang)
seno = sin(rad)
tangente = tan(rad)
cosen = cos(rad)
print('O cosseno de {:.2f} é igual a {:.2f} \n O seno e igual a {:.2f} \n A tangente é {:.2f}.'.format(ang, cosen, seno, tangente))