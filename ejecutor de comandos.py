import subprocess

comando = input("Escriba el comando a ejecutar:  ").split()


try:
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print(resultado.stdout)
    
    
except FileNotFoundError:
    print("Archivo no encontrado")