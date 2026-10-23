from pathlib import Path


class GeneradorResumenTXT:
    def __init__(self, resultados_csv, resultados_json):
        self.resultados_csv = resultados_csv
        self.resultados_json = resultados_json

    def generar_resumen(self):
        """Construye el resumen usando los resultados reales."""

        lineas = ["ACTIVIDAD 2 - MANEJO DE ARCHIVOS CSV, JSON Y TXT", "=" * 60, ""]

        for formato, resultado in [
            ("CSV", self.resultados_csv),
            ("JSON", self.resultados_json),
        ]:
            lineas.extend(
                [
                    f"ARCHIVO {formato}",
                    "-" * 60,
                    f"URL de origen: {resultado['url_origen']}",
                    f"Archivo importado: {resultado['archivo_original']}",
                    f"Archivo guardado: {resultado['archivo_modificado']}",
                    f"Registros procesados: {resultado['registros_procesados']}",
                    f"Clase utilizada: {resultado['clase']}",
                    "Metodos utilizados:",
                ]
            )

            for metodo in resultado["metodos"]:
                lineas.append(f"  - {metodo}")

            lineas.append("Modificaciones realizadas:")

            for modificacion in resultado["modificaciones"]:
                lineas.append(f"  - {modificacion}")

            lineas.append("")

        return "\n".join(lineas)

    def guardar_resumen(self, ruta_salida):
        """Genera y guarda el resumen en formato TXT."""
        ruta_salida = Path(ruta_salida)
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)

        contenido = self.generar_resumen()

        with open(ruta_salida, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)

        return ruta_salida
