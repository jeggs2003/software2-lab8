# app.py (Versión 4.0 Final - Arquitectura completa con Flags)
import datetime
import json  

FEATURE_V2_ENABLED = True
FEATURE_V3_ENABLED = True
FEATURE_V4_ENABLED = True 

def guardar_log(accion, usuario="Sistema", nivel="INFO"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if FEATURE_V4_ENABLED:
        log_data = {
            "timestamp": timestamp,
            "level": nivel,
            "user": usuario,
            "action": accion
        }
        log_line = json.dumps(log_data)
    else:
        # Formato de texto legacy (v2/v3)
        log_line = f"[{timestamp}] - {accion}"
        
    with open("app_log.txt", "a") as f:
        f.write(log_line + "\n")

def ejecutar_legacy():
    print("[INFO] Ejecutando modo de compatibilidad v3.0...")
    # ... (Si apagas la v4, el comportamiento volvería al menú anterior)

def main():
    if not FEATURE_V4_ENABLED:
        ejecutar_legacy() # Degradación elegante
        return
    while True:
        print("\n⚡=== Enterprise Greeting Platform v4.0 (JSON Logs Enabled) ===⚡")
        print("1. Saludo Personalizado")
        print("2. Visualizar Logs en crudo (JSON)")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            nombre = input("Ingresa tu nombre: ").strip()
            if not nombre:
                print("❌ El nombre es requerido.")
                guardar_log("Validación fallida: Nombre vacío", nivel="WARNING")
                continue
                
            tono = input("Elige el tono del saludo (1: Formal / 2: Informal): ").strip()
            
            if tono == "1":
                print(f"Estimado/a {nombre}, es un honor darle la bienvenida al sistema v4.0.")
                guardar_log("Saludo formal generado", usuario=nombre)
            else:
                print(f"¡Qué onda, {nombre}! Todo bien en la v4.0? 🔥")
                guardar_log("Saludo informal generado", usuario=nombre)
                
        elif opcion == "2":
            print("\n📋 --- Logs Estructurados Registrados ---")
            try:
                with open("app_log.txt", "r") as f:
                    for linea in f:
                        print(linea.strip())
            except FileNotFoundError:
                print("No hay registros.")
                
        elif opcion == "3":
            print("Finalizando plataforma v4.0.")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()