a = 80000
b = 200000
ano  = 0
while a < b:
    a = (0.03 * a) + a
    b = (0.015 * b) + b
    ano += 1
print(f'Vai demorar {ano} anos para A ficar com a população maior que B.')