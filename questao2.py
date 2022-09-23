n = int(input())
lista_perfeitos = []
lista_nao_perfeitos = []
for i in range(n):
    x = int(input())
    soma = 0
    for j in range(1, x):
        if x % j == 0:
            soma += j
    if soma == x:
        lista_perfeitos.append(x)
    else : lista_nao_perfeitos.append(x)
print(f'perfeitos = {lista_perfeitos}')
print(f'não-perfeitos = {lista_nao_perfeitos}')