""" 
Dois carros (X e Y)
X = 60km/h
Y = 90km/h

em uma hora o carro Y se distancia 30km do carro X,
ou seja, 2km a cada 2 minutos

quanto tempo leva (em minutos) para o carro Y tomar essa
distância?
"""

CARRO_X = 60
CARRO_Y = 90
distancia_carros = (CARRO_Y / 60) - (CARRO_X / 60)
distancia_km = int(input())

print("%d minutos" % (distancia_km / distancia_carros))