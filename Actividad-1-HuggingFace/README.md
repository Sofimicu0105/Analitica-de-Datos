# Actividad 1 – Obtención y preparación de datos desde Hugging Face

## Descripción

En esta actividad se desarrolla un programa en Python que permite cargar un dataset desde Hugging Face, convertirlo en un DataFrame de pandas, aplicar diferentes transformaciones y generar un archivo TXT con un resumen de los datos procesados.

El desarrollo utiliza programación orientada a objetos y un notebook de Jupyter para coordinar la ejecución.

## Tecnologías utilizadas

- Python
- Pandas
- Hugging Face Datasets
- Jupyter Notebook
- Git y GitHub

## Dataset seleccionado

Se utilizó el dataset `scikit-learn/iris`, disponible en Hugging Face.

El dataset original contiene 150 registros y 6 columnas relacionadas con las medidas de sépalos y pétalos de diferentes especies de flores.

## Clases implementadas

**HFDatasetLoader:** recibe el identificador del dataset y el split, carga los datos desde Hugging Face y los convierte en un DataFrame de pandas.

**DatasetSummarizer:** recibe un DataFrame y genera un archivo de texto con información sobre las filas, columnas, tipos de datos, valores nulos y estadísticas descriptivas.

## Transformaciones realizadas

1. **Renombrar columnas:** se cambiaron los nombres originales de las columnas por nombres en español.
2. **Filtrar registros:** se conservaron únicamente los registros cuyo largo del pétalo fuera mayor que 2 cm.
3. **Crear una columna:** se calculó el área aproximada del pétalo multiplicando su largo por su ancho.
4. **Ordenar registros:** se organizaron los datos de mayor a menor según el largo del pétalo y se reinició el índice.

Después de las transformaciones, el DataFrame contiene 100 registros y 7 columnas.

## Archivos del proyecto

- `hf_dataset_loader.py`: clase para cargar datasets desde Hugging Face.
- `dataset_summarizer.py`: clase para generar el resumen.
- `probar_carga.py`: archivo para realizar pruebas.
- `actividad_1_huggingface.ipynb`: notebook con el desarrollo completo.
- `resumen_dataset.txt`: resumen generado a partir de los datos transformados.
- `requirements.txt`: dependencias del proyecto.

## Instrucciones de ejecución

1. Clonar el repositorio:

   `git clone https://github.com/Sofimicu0105/Analitica-de-Datos.git`

2. Ingresar a la carpeta `Actividad-1-HuggingFace`.

3. Crear y activar un entorno virtual de Python.

4. Instalar las dependencias mediante `pip install -r requirements.txt`.

5. Abrir `actividad_1_huggingface.ipynb` en VS Code o Jupyter Notebook.

6. Seleccionar el kernel de Python y ejecutar todas las celdas en orden.

7. Verificar que se genere el archivo `resumen_dataset.txt`.

## Resultados

Se logró cargar correctamente el dataset Iris, aplicar cuatro transformaciones y generar un resumen automático utilizando las clases desarrolladas en Python.

El proyecto conserva su código fuente y el historial de cambios en GitHub.