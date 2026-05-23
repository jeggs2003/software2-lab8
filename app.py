# app.py (Versión 3.0 con Feature Flags Acumulativos)
import datetime

# FEATURE FLAGS (Permiten activar o degradar funciones en paralelo)
FEATURE_V2_ENABLED = True
FEATURE_V3_ENABLED = True  # <- Nueva bandera para el menú y validaciones

def guardar_log(accion):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app_log.txt", "a") as f:
        f.write(f"[{timestamp}] - {accion}\n")

def ejecutar_v1_v2():
    """Mantiene la compatibilidad con el comportamiento de v1 y v2"""
    print("=== Aplicación de Saludos v1.0 / v2.0 (Legacy Mode) ===")
    if not FEATURE_V2_ENABLED:
        nombre = input("Por favor, ingresa tu nombre: ")
        print(f"¡Hola, {nombre}! Bienvenido al sistema.")
        return
    
    idioma = input("Selecciona idioma / Select language (ES/EN): ").strip().upper()
    nombre = input("Ingresa tu nombre / Enter your name: ")
    saludo = f"Hello, {nombre}!" if idioma == "EN" else f"¡Hola, {nombre}!"
    print(saludo)
    guardar_log(f"Ejecución Legacy v2 en idioma [{idioma}].")

def main():
    # Si la v3 está apagada, degrada automáticamente a la lógica anterior
    if not FEATURE_V3_ENABLED:
        ejecutar_v1_v2()
        return

    # --- LÓGICA NUEVA DE LA V3.0 ---
    while True:
        print("\n=== Sistema de Saludos Avanzado v3.0 ===")
        print("1. Ejecutar Saludo")
        print("2. Ver logs de auditoría")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            idioma = input("Selecciona idioma (ES/EN): ").strip().upper()
            nombre = input("Ingresa tu nombre: ").strip()
            
            # Validación de datos (Robustez de la v3)
            if not nombre:
                print("[ERROR] El nombre no puede estar vacío. Inténtalo de nuevo.")
                guardar_log("Intento de registro fallido: Nombre vacío.")
                continue
                
            if idioma == "EN":
                print(f"Hello, {nombre}! Welcome to version 3.0.")
            else:
                print(f"¡Hola, {nombre}! Bienvenido a la versión 3.0.")
            guardar_log(f"Usuario '{nombre}' saludado exitosamente en [{idioma}].")
            
        elif opcion == "2":
            print("\n--- Leyendo Logs de Auditoría ---")
            try:
                with open("app_log.txt", "r") as f:
                    print(f.read())
            except FileNotFoundError:
                print("[INFO] No hay logs registrados todavía.")
                
        elif opcion == "3":
            print("Saliendo del sistema v3.0. ¡Adiós!")
            break
        else:
            print("[ERROR] Opción inválida. Elige 1, 2 o 3.")

if __name__ == "__main__":
    main()