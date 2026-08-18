#descubir que {indice + 1} en una str sirve para enumerar una lista o bucle repetido
invitados = []
for indice in range(5):
    nombre = input(f'ingrese el nombre del invitado #{indice + 1}')
    invitados.append(nombre)
for indice, nombre in enumerate(invitados):
 print(f'invitado {indice + 1}: {nombre}')