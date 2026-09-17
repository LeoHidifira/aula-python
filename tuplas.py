# Crie uma maneira de adicionar elementos em uma tupla. 
# Sua função recebe a tupla e o elemento a ser adicionado e retorna a tupla final.

tupla = (1,2,3,4)

def add_tupla(var):
    return tupla + (var,)


print(add_tupla(5))


# Crie uma maneira para remover elementos em uma tupla.
# Sua função recebe a tupla e o index do elemento a ser removido e retorna a tupla final.


def rem_tupla(tupla, index):
    a = list(tupla)
    a.pop(index)
    return tuple(a)

