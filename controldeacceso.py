USUARIO_VALIDO = "DANIel19"
CONTRASENA_VALIDA = "12345"

usercode = input("Write your username").strip()
if usercode == "":
    exit("Username can't be empty, please write a valid username")
if usercode == USUARIO_VALIDO:
    print("Is a valid Username, can procced")
else:
    exit("This is not a valid username")

password = input("Write your password").strip()
if password == "":
    exit("Password can't be empty, please write a valid password")
if password == CONTRASENA_VALIDA:
    print("Valid password")
    print("Access granted, welcome")
else:
    exit("Invalid password can't proceed")

