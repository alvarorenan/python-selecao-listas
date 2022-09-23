n = int(input())
hipotenusa = n;
catetob, catetoc = 0, 0
for i in range(1, n):
    for j in range(1, n):
        if i**2 + j**2 == hipotenusa**2:
            catetob = i
            catetoc = j
            break;
print(f'Tripla: {catetob} {catetoc} {hipotenusa}')