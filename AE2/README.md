# Actividad 2 – Manejo de archivos CSV, JSON y TXT

## Descripción

En esta actividad se desarrolla un programa en Python para importar, modificar y guardar archivos CSV y JSON, utilizando programación orientada a objetos.

También se implementa una clase para generar automáticamente un archivo TXT con el resumen del procesamiento realizado.

El desarrollo se integra en un notebook de Jupyter, donde se ejecutan las clases y se verifican los resultados.

## Tecnologías utilizadas

- Python
- Librerías `csv` y `json`
- `pathlib` para el manejo de rutas
- Jupyter Notebook
- Git y GitHub

## Archivos seleccionados

Los archivos utilizados se obtuvieron de datasets disponibles en Hugging Face.

**Archivo CSV**

- Dataset: `copenlu/spiced`
- Archivo: `dev.csv`
- URL: https://huggingface.co/datasets/copenlu/spiced/resolve/main/dev.csv
- Registros procesados: 664

**Archivo JSON**

- Dataset: `BreezeBlue/TTS-Voice-Design-Benchmark`
- Archivo descargado: `tts_voice_design_dataset.jsonl`
- URL: https://huggingface.co/datasets/BreezeBlue/TTS-Voice-Design-Benchmark/resolve/main/tts_voice_design_dataset.jsonl
- Registros procesados: 1000

El segundo archivo se descargó originalmente en formato JSONL y posteriormente se convirtió a JSON mediante el script `convertir_jsonl.py`.

## Clases implementadas

### ManejadorCSV

Permite importar un archivo CSV, modificar un registro y guardar los cambios en un archivo diferente.

Métodos utilizados:

- `importar_csv()`
- `modificar_registro()`
- `guardar_csv()`

### ManejadorJSON

Permite importar un archivo JSON, modificar un campo de un registro y guardar el resultado sin sobrescribir el archivo original.

Métodos utilizados:

- `importar_json()`
- `modificar_registro()`
- `guardar_json()`

### GeneradorResumenTXT

Genera un resumen en formato TXT que contiene las fuentes de los archivos, las rutas utilizadas, la cantidad de registros procesados, las clases y métodos ejecutados y las modificaciones realizadas.

Métodos utilizados:

- `generar_resumen()`
- `guardar_resumen()`

## Modificaciones realizadas

**CSV:** se modificó el campo `News Finding` del primer registro, reemplazando su contenido por el texto `Registro actualizado para la Actividad 2`.

**JSON:** se modificó el campo `language` del primer registro, cambiando su valor de `en` a `es`. Este cambio corresponde a una modificación de prueba y no implica la traducción del contenido.

En ambos casos, los archivos originales se conservaron y los resultados se guardaron en la carpeta `datos_modificados`.

## Estructura del proyecto

```text
AE2/
├── datos_originales/
│   ├── dev.csv
│   ├── tts_voice_design_dataset.jsonl
│   └── tts_voice_design_dataset.json
├── datos_modificados/
│   ├── dev_modificado.csv
│   └── tts_voice_design_modificado.json
├── manejador_csv.py
├── manejador_json.py
├── generador_resumen_txt.py
├── convertir_jsonl.py
├── probar_csv.py
├── probar_json.py
├── actividad_2.ipynb
├── resumen.txt
└── README.md
```

## Instrucciones de ejecución

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Sofimicu0105/Analitica-de-Datos.git
   ```

2. Abrir el proyecto en VS Code.

3. Seleccionar un entorno de Python con Jupyter instalado.

4. Abrir `AE2/actividad_2.ipynb`.

5. Seleccionar el kernel de Python.

6. Ejecutar todas las celdas en orden.

7. Verificar que se generen los archivos modificados y `resumen.txt`.

## Resultados obtenidos

Se procesaron correctamente 664 registros CSV y 1000 registros JSON.

Se realizaron modificaciones controladas en ambos formatos y se guardaron los resultados en archivos independientes.

Finalmente, se generó automáticamente `resumen.txt` y se verificó que los archivos originales conservaran sus valores.

## Conclusión

La actividad permitió aplicar programación orientada a objetos para trabajar con diferentes formatos de archivos, organizar el procesamiento de datos mediante clases y documentar los resultados obtenidos.

El uso de Jupyter Notebook facilitó la integración, ejecución y verificación de todo el proceso.
