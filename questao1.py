n = int(input())
lista_teto = []
for i in range(n):
    x = float(input())
    x_teto = int(x)
    if x_teto < x:
        x_teto += 1
    lista_teto.append(x_teto)
print(' '.join(map(str, lista_teto)))