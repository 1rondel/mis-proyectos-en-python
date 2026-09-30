import subprocess

red = input("Ingrese los primeros 3 octetos de la red (ej: 192.168.1): ")
activas = 0
for i in range(1,11):
    ip = f"{red}.{i}"
    
    try:
     resultado = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True, timeout=2)
     if resultado.returncode == 0:
        print(f"{ip}:  ACTIVA")
        activas += 1
    except subprocess.TimeoutExpired:
      pass    
print(f"se encontraron {activas} IPs activas")