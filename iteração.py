# l = [12, 68, 95, 41, 25, 71]
# print(l)

# for j in range(len(l)-1,0,-1):
#     for i in range(j):
#         if l[i] > l[i+1]:
#             aux = l[i]
#             l[i] = l[i + 1]
#             l[i + 1] = aux
#         print(l)
#     print()


# selection sort
l = [12, 68, 95, 41, 10, 71]
print(l)

def index_menor(index_partida,l):
    imenor = index_partida
    menor_elemento = l[imenor]
    for i in range(imenor, len(l)):
        if l[i] < menor_elemento:
            menor_elemento = l[i]
            imenor = i
    return imenor

for k in range(len(l)):
    j = index_menor(k,l)
    aux = l[j]
    l[j] = l[k]
    l[k] = aux
    print(l)


# Insertion sort

# 1- Crie uma função que, dado ima lista e uma indice i, insete o elemento de indice i entre os elementos
# das posições 0 e i-1 (pré-ordenados), de forma que todos elementos continuem ordenados 


# Crie o algoritmo