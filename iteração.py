l = [12, 68, 95, 41, 25, 71]
print(l)

for j in range(len(l)-1,0,-1):
    for i in range(j):
        if l[i] > l[i+1]:
            aux = l[i]
            l[i] = l[i + 1]
            l[i + 1] = aux
        print(l)
    print()