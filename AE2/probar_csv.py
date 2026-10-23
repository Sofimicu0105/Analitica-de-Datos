import csv
from pathlib import Path

from manejador_csv import ManejadorCSV

# Rutas relativas a la carpeta AE2
base = Path(__file__).resolve().parent

ruta_original = base / "datos_originales" / "dev.csv"
ruta_modificada = base / "datos_modificados" / "dev_modificado.csv"

# 1. Importar el CSV
manejador = ManejadorCSV(ruta_original)
registros = manejador.importar_csv()

# 2. Mostrar el valor original
indice_columna = manejador.encabezados.index("News Finding")
print("\nVALOR ORIGINAL:")
print(registros[0][indice_columna])

# 3. Modificar un registro utilizando la clase
resultado = manejador.modificar_registro(
    indice=0,
    columna="News Finding",
    nuevo_valor="Registro actualizado para la Actividad 2",
)

print("\nMODIFICACION REALIZADA:")
print(resultado)

# 4. Guardar un nuevo CSV
manejador.guardar_csv(ruta_modificada)

# 5. Verificar el archivo generado
with open(ruta_modificada, "r", encoding="utf-8", newline="") as archivo:
    lector = csv.reader(archivo)
    encabezados_guardados = next(lector)
    primer_registro = next(lector)

assert encabezados_guardados == manejador.encabezados
assert primer_registro[indice_columna] == resultado["valor_nuevo"]

print("\nVERIFICACION EXITOSA")
print("Registros procesados:", len(manejador.registros))
print("Archivo original:", ruta_original)
print("Archivo modificado:", ruta_modificada)
