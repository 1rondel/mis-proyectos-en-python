def most_frequent(data: list[str]) -> str:
    conteo = {}
    
    # Corregido: Recorremos la lista 'data' usando la variable 'elemento'
    for elemento in data:
        if elemento in conteo:
            conteo[elemento] = conteo[elemento] + 1
        else:
             conteo[elemento] = 1
             
    ganador = ""
    max_val = 0
    
    # Corregido: Se quitó la 'e' extra de conteeo y se agregaron los dos puntos (:)
    for elemento, numero in conteo.items():
        # Corregido: Se agregaron los dos puntos (:)
        if numero > max_val:
            # Corregido: Usamos max_val para guardar el récord
            max_val = numero
            ganador = elemento
   
    return ganador