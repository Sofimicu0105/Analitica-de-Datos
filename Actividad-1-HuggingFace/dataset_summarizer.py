from pathlib import Path

import pandas as pd


class DatasetSummarizer:
    def __init__(self, dataframe, nombre_dataset="Dataset"):
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Los datos deben ser un DataFrame de pandas.")

        self.dataframe = dataframe
        self.nombre_dataset = nombre_dataset

    def generar_resumen(self):
        """Construye un resumen con la información del DataFrame."""
        df = self.dataframe

        resumen = [
            f"RESUMEN DEL DATASET: {self.nombre_dataset}",
            "=" * 50,
            f"Cantidad de filas: {df.shape[0]}",
            f"Cantidad de columnas: {df.shape[1]}",
            "",
            "COLUMNAS Y TIPOS DE DATOS",
            "-" * 50,
        ]

        for columna, tipo in df.dtypes.items():
            resumen.append(f"{columna}: {tipo}")

        resumen.extend(
            [
                "",
                "VALORES NULOS POR COLUMNA",
                "-" * 50,
            ]
        )

        for columna, cantidad in df.isnull().sum().items():
            resumen.append(f"{columna}: {cantidad}")

        resumen.extend(
            [
                "",
                "ESTADISTICAS DESCRIPTIVAS",
                "-" * 50,
            ]
        )

        columnas_numericas = df.select_dtypes(include="number")

        if not columnas_numericas.empty:
            resumen.append(columnas_numericas.describe().to_string())
        else:
            resumen.append("No hay datos numericos para analizar.")

        return "\n".join(resumen)

    def guardar_resumen(self, ruta_archivo="resumen_dataset.txt"):
        """Guarda el resumen generado en un archivo de texto."""
        ruta = Path(ruta_archivo)
        ruta.parent.mkdir(parents=True, exist_ok=True)

        contenido = self.generar_resumen()
        ruta.write_text(contenido, encoding="utf-8")

        return ruta
