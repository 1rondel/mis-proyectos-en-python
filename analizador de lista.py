lista = [1, 2, 3, 4]

def analizador_de_lista(lista):
    if not lista :
        return None
    else :  
        promedio = (sum(lista) / len(lista))
        return sum(lista), promedio, max(lista)  # Devuelve una tupla

resultado = analizador_de_lista(lista)
print(resultado)