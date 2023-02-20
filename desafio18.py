import math
a = float(input('Valor do angulo:'))

seno = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print(f'O angulo {a} \nTem o seno de {seno:.2f} \nO cosseno de {cos:.2f} \nE a tangente de {tan:.2f}')