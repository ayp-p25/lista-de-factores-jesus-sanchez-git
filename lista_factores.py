def es_factor(Num):
    factores = []
    for i in range(1, Num+1):
        if Num % i == 0:
            factores.append(i)
    return factores
Num = int(input("Escriba el numero del que quisiera saber sus factores: \n"))
factores = es_factor(Num)
print(f"Los factores de {Num} son : {factores}")