# app.py (Versión 2.0 con Feature Flag)
import datetime


FEATURE_V2_ENABLED = True

def guardar_log(accion):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app_log.txt", "a") as f:
        f.write(f"[{timestamp}] - {accion}\n")

def main():
    if not FEATURE_V2_ENABLED:
        # Comportamiento heredado de la v1.0
        print("=== Aplicación de Saludos v1.0 (Legacy Mode) ===")
        nombre = input("Por favor, ingresa tu nombre: ")
        print(f"¡Hola, {nombre}! Bienvenido al sistema.")
        return

    # Características nuevas de la v2.0
    print("=== Aplicación de Saludos Premium v2.0 ===")
    idioma = input("Selecciona idioma / Select language (ES/EN): ").strip().upper()
    nombre = input("Ingresa tu nombre / Enter your name: ")

    if idioma == "EN":
        saludo = f"Hello, {nombre}! Welcome to the advanced system."
    else:
        saludo = f"¡Hola, {nombre}! Bienvenido al sistema avanzado."

    print(saludo)
    guardar_log(f"Usuario '{nombre}' ejecutó la app en idioma [{idioma}].")

if __name__ == "__main__":
    main()