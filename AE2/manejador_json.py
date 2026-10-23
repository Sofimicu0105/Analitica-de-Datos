import json
from pathlib import Path


class ManejadorJSON:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = Path(ruta_archivo)
        self.registros = []
        self.modificaciones = []

    def importar_json(self):
        """Importa los registros utilizando json.load."""
        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, list):
            raise ValueError("El JSON debe contener una lista.")

        if not all(isinstance(registro, dict) for registro in datos):
            raise ValueError("Los registros deben ser objetos JSON.")

        self.registros = datos
        self.modificaciones = []

        print(f"Archivo importado: {self.ruta_archivo.name}")
        print(f"Registros cargados: {len(self.registros)}")

        return self.registros

    def modificar_registro(self, indice, campo, nuevo_valor):
        """Actualiza un campo de un registro."""
        if not 0 <= indice < len(self.registros):
            raise IndexError("Índice de registro no válido.")

        if campo not in self.registros[indice]:
            raise ValueError(f"El campo '{campo}' no existe.")

        valor_anterior = self.registros[indice][campo]
        self.registros[indice][campo] = nuevo_valor

        cambio = {
            "indice": indice,
            "campo": campo,
            "valor_anterior": valor_anterior,
            "valor_nuevo": nuevo_valor,
        }

        self.modificaciones.append(cambio)
        return cambio

    def guardar_json(self, ruta_salida):
        """Guarda los registros en un archivo JSON nuevo."""
        ruta_salida = Path(ruta_salida)

        if ruta_salida.resolve() == self.ruta_archivo.resolve():
            raise ValueError("No se puede sobrescribir el JSON original.")

        ruta_salida.parent.mkdir(parents=True, exist_ok=True)

        with open(ruta_salida, "w", encoding="utf-8") as archivo:
            json.dump(self.registros, archivo, ensure_ascii=False, indent=2)

        print(f"Archivo guardado: {ruta_salida}")
        return ruta_salida
