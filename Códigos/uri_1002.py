""" 
Entrada
A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.

Saída
Apresentar a mensagem "A=" seguido pelo valor da variável area, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double).
"""

raio = float(input())
N = 3.14159

area = N * raio ** 2

#print(f"A=",round(area, 4))

print(f"A=%.4f" % area)