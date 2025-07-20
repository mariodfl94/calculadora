#saca los numeros primos de un determinado numero

n = int(input());
c=0
p=0
while c <= n:
    c += 1
    if n % c == 0:
        p += 1
if p<= 2:
    print("Es primo")
else:
    print("No es primo")