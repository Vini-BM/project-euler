import numpy as np

#Sem arredondar os números originais
num = np.loadtxt('euler013_file.txt')
soma = int(np.sum(num))
res = str(soma)
print(res[0:10])

#Arredondando os números originais
file = open('euler013_file.txt')
numeros = []
for line in file:
    int_line = int(line[0:12])
    numeros.append(int_line)
soma = 0
for num in numeros:
    soma += num
res = str(soma)
print(res[0:10])
