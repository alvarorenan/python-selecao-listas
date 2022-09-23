n = int(input())
primo = True;
sophie = True;
if n==1:
    sophie = False
    primo = False
for i in range(2, n):
    if n%i == 0:
       primo = False;
       break
if primo:
    for i in range(2, n*2+1):
        if (n*2+1)%i == 0:
            sophie = False;
            break
if primo and sophie:
    print('Numero primo de Sophie-Germain')
elif primo:
    print('Numero primo')
else:
    print('Numero nao primo')





