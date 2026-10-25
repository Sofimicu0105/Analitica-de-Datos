# Proyecto Integrador EA2 – Análisis Descriptivo de Ventas

## 1. Descripción del proyecto

Este proyecto se desarrolla como parte de la asignatura Analítica de Datos de la IU Digital de Antioquia.

Su propósito es realizar una exploración inicial de un conjunto de datos de ventas comerciales obtenido desde Hugging Face, utilizando Python, Pandas y Jupyter Notebook.

El proyecto busca establecer las bases para un análisis descriptivo que permita comprender cómo se distribuyen las ventas según las categorías de productos, los tipos de establecimientos y las ubicaciones.

## 2. Necesidad analítica

En un escenario empresarial hipotético, una organización comercial requiere conocer qué categorías de productos y tipos de establecimientos presentan mayores ventas registradas.

Esta información permitiría identificar diferencias en el comportamiento comercial y servir como apoyo para futuras decisiones relacionadas con la gestión de productos y establecimientos.

**Pregunta de análisis:**

¿Qué categorías de productos y tipos de establecimientos presentan mayores ventas registradas en el dataset SuperKart?

## 3. Dataset utilizado

- **Nombre:** SuperKart Sales Dataset.
- **Identificador:** `dev02chandan/sales-forecast-dataset`
- **Fuente:** [Hugging Face](https://huggingface.co/datasets/dev02chandan/sales-forecast-dataset)
- **Split utilizado:** `train`
- **Cantidad de registros:** 7.414
- **Cantidad de columnas:** 12
- **Valores nulos:** 0

Se utiliza el conjunto completo correspondiente al split `train`, sin aplicar muestreo.

## 4. Herramientas utilizadas

- Python
- Pandas
- Hugging Face Datasets
- Jupyter Notebook
- Git y GitHub
- Visual Studio Code

## 5. Estructura del proyecto

```text
Proyecto-Integrador-EA2/
├── documento/
├── notebooks/
│   └── exploracion_ventas.ipynb
├── resultados/
│   └── resumen_dataframe.txt
├── src/
├── requirements.txt
└── README.md
```

## 6. Ejecución del proyecto

1. Clonar el repositorio de GitHub.
2. Abrir la carpeta `Proyecto-Integrador-EA2` en Visual Studio Code.
3. Crear y activar un entorno virtual de Python.
4. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

5. Abrir el notebook `notebooks/exploracion_ventas.ipynb`.
6. Seleccionar el intérprete de Python del entorno virtual.
7. Ejecutar las celdas en orden.

El notebook obtiene los datos desde Hugging Face, los convierte en un DataFrame de Pandas y presenta una descripción básica de sus características.

Finalmente, genera automáticamente el archivo `resultados/resumen_dataframe.txt`.

## 7. Resultados iniciales

La exploración del dataset permitió identificar:

- 7.414 registros en el split `train`.
- 12 variables relacionadas con productos, establecimientos y ventas.
- Ausencia de valores nulos en las columnas analizadas.
- Variables categóricas y numéricas que permiten desarrollar un análisis descriptivo de las ventas.

## 8. Alcance

Esta primera etapa se concentra en la identificación de una necesidad analítica y el reconocimiento de los datos disponibles.

No se realizan modelos predictivos ni se pretende demostrar relaciones causales. Los resultados posteriores deberán interpretarse considerando las características y limitaciones del dataset.

## 9. Referencias

- Hugging Face. SuperKart Sales Dataset. https://huggingface.co/datasets/dev02chandan/sales-forecast-dataset
- Pandas. Documentación oficial. https://pandas.pydata.org/docs/