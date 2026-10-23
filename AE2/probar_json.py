import json
from pathlib import Path

from manejador_json import ManejadorJSON

# Rutas de los archivos
base = Path(__file__).resolve().parent

ruta_original = base / "datos_originales" / "tts_voice_design_dataset.json"

ruta_modificada = base / "datos_modificados" / "tts_voice_design_modificado.json"

# 1. Importar el archivo JSON
manejador = ManejadorJSON(ruta_original)
registros = manejador.importar_json()

# 2. Mostrar el valor original
print("\nREGISTRO ORIGINAL:")
print(json.dumps(registros[0], indent=2, ensure_ascii=False))

# 3. Modificar un registro mediante la clase
resultado = manejador.modificar_registro(indice=0, campo="language", nuevo_valor="es")

print("\nMODIFICACION REALIZADA:")
print(resultado)

# 4. Mostrar el registro modificado
print("\nREGISTRO MODIFICADO:")
print(json.dumps(registros[0], indent=2, ensure_ascii=False))

# 5. Guardar el nuevo archivo JSON
manejador.guardar_json(ruta_modificada)

# 6. Verificar que el cambio quedó guardado
with open(ruta_modificada, "r", encoding="utf-8") as archivo:
    datos_guardados = json.load(archivo)

with open(ruta_original, "r", encoding="utf-8") as archivo:
    datos_originales = json.load(archivo)

assert len(datos_guardados) == len(datos_originales)
assert datos_originales[0]["language"] == "en"
assert datos_guardados[0]["language"] == "es"

print("\nVERIFICACION EXITOSA")
print("Registros procesados:", len(datos_guardados))
print("Archivo original:", ruta_original)
print("Archivo modificado:", ruta_modificada)
