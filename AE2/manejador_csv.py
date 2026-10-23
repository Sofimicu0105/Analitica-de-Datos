import csv
from pathlib import Path


class ManejadorCSV:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = Path(ruta_archivo)
        self.encabezados = []
        self.registros = []
        self.modificaciones = []

    def importar_csv(self):
        """Importa el archivo CSV y conserva sus encabezados."""
        with open(self.ruta_archivo, "r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.reader(archivo)
            self.encabezados = next(lector)
            self.registros = list(lector)

        print(f"Archivo importado: {self.ruta_archivo.name}")
        print(f"Registros cargados: {len(self.registros)}")

        return self.registros

    def modificar_registro(self, indice, columna, nuevo_valor):
        """Modifica el valor de una columna en un registro."""
        if columna not in self.encabezados:
            raise ValueError(f"La columna '{columna}' no existe.")

        if indice < 0 or indice >= len(self.registros):
            raise IndexError("El índice del registro no es válido.")

        posicion_columna = self.encabezados.index(columna)
        valor_anterior = self.registros[indice][posicion_columna]

        self.registros[indice][posicion_columna] = str(nuevo_valor)

        descripcion = (
            f"Registro {indice}, columna '{columna}': "
            f"'{valor_anterior}' -> '{nuevo_valor}'"
        )

        self.modificaciones.append(descripcion)

        return {
            "indice": indice,
            "columna": columna,
            "valor_anterior": valor_anterior,
            "valor_nuevo": nuevo_valor,
        }

    def guardar_csv(self, ruta_salida):
        """Guarda los datos modificados en un nuevo CSV."""
        ruta_salida = Path(ruta_salida)
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)

        if ruta_salida.resolve() == self.ruta_archivo.resolve():
            raise ValueError("No se puede sobrescribir el archivo original.")

        with open(ruta_salida, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.encabezados)
            escritor.writerows(self.registros)

        print(f"Archivo guardado: {ruta_salida}")
        return ruta_salida
