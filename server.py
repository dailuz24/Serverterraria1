import subprocess
import os

def start_terraria_server():
    # Ruta al archivo TerrariaServer.exe
    server_path = "terraria_files/TerrariaServer.exe"

    if os.path.exists(server_path):
        print("Iniciando el servidor de Terraria...")
        subprocess.run([server_path])
    else:
        print(f"No se encontró el archivo {server_path}. Asegúrate de que el archivo esté en la ubicación correcta.")

if __name__ == "__main__":
    start_terraria_server()
