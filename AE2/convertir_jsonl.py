import json
from pathlib import Path

carpeta = Path(__file__).resolve().parent / "datos_originales"

archivo_origen = carpeta / "tts_voice_design_dataset.jsonl"
archivo_destino = carpeta / "tts_voice_design_dataset.json"

registros = []

with open(archivo_origen, "r", encoding="utf-8") as archivo:
    for numero_linea, linea in enumerate(archivo, start=1):
        if linea.strip():
            try:
                registros.append(json.loads(linea))
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"Error en la línea {numero_linea}: {error}"
                ) from error

with open(archivo_destino, "w", encoding="utf-8") as archivo:
    json.dump(registros, archivo, ensure_ascii=False, indent=2)

print("Conversión completada correctamente.")
print("Registros convertidos:", len(registros))
print("Archivo generado:", archivo_destino)
