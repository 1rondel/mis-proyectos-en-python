contactos = {
 "pepito":{"telefono":"123-456-7890", "email":"pepito@example.com"},
 "maria":{"telefono":"098-765-4321", "email":"maria@example.com"},
 "juan":{"telefono":"555-555-5555", "email":"juan@example.com"}
   
}

    

while True:
    print("1. Buscar contacto")
    print("2. Ver todos")
    print("3. agregar contacto")
    print("4. Salir")
    opcion = input("Elige: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        if not nombre:
            print("No se ingresó ningún nombre")
            continue
        if nombre in contactos:
            print("Teléfono:", contactos[nombre]["telefono"])
            print("Email:", contactos[nombre]["email"])
        else:
            print("Contacto no encontrado")
            opcion2 = input('deseea agregarlo? s/n: ').lower()
            if opcion2 == "s":
                telfono = input("Ingrese el teléfono del contacto: ")
                email = input("Ingrese el email del contacto: ")
                contactos[nombre] = {"telefono": telfono, "email": email}
                print("Contacto agregado exitosamente")
                print("Contactos actuales: ", contactos)
            else:
                print("No se agregó el contacto")
    elif opcion == "2":
        print("Contactos actuales`: ", contactos)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto: ")
        if not nombre:
            print("No se ingresó ningún nombre")
            continue
        telfono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        contactos[nombre] = {"telefono": telfono, "email": email}
        print("Contacto agregado exitosamente")
        print("Contactos actuales: ", contactos)
    elif opcion == "4":
        break
    else:
        print("Opción no válida")