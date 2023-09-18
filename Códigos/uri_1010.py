"""
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
"""
cod_peca_1, num_peca_1, valor_unitario_peca_1 = input().split(" ")
cod_peca_1 = int(cod_peca_1) 
num_peca_1 = int(num_peca_1) 
valor_unitario_peca_1 = float(valor_unitario_peca_1)

cod_peca_2, num_peca_2, valor_unitario_peca_2 = input().split(" ")
cod_peca_2 = int(cod_peca_2) 
num_peca_2 = int(num_peca_2) 
valor_unitario_peca_2 = float(valor_unitario_peca_2)

valor_pagar = valor_unitario_peca_1 * num_peca_1 + valor_unitario_peca_2 * num_peca_2
print(f"VALOR A PAGAR: R$ %.2f" % valor_pagar)

