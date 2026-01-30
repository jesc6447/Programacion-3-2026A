# Juan Emmanuel Sanchez Castañon
# Tipos de datos en Python: listas y sus manipulaciones

c = ['a', 1, 'd', 'Colores', False, 3.9, 14, True, False, 88, 4.2]

print(c)

for i, elemento in enumerate(c):
    if type(elemento) == bool:
        c[i] = not elemento
    elif type(elemento) == int:
        c[i] = elemento + 10
    elif type(elemento) == float:
        c[i] = elemento + 2.5

print(c)