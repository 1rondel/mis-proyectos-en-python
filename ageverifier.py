try:
 edad = int(input("Escriba su edad: "))

 if edad >= 18:
     print("Usted es mayor de edad puede pasar")
 else:
     print("Usted es menor de edad no puede pasar")

 Paisderesidencia = input("Escriba su país de residencia: ").lower()
 if Paisderesidencia == "republica dominicana" and edad >= 18:
     print("Usted puede votar en las elecciones de la Republica Dominicana")

 else:
     print("Usted no puede votar en las elecciones de la Republica Dominicana")
except ValueError:
    print("Por favor, ingrese un número válido para la edad.")