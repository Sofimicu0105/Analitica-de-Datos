# SuperKart Analytics | Proyecto Integrador

Análisis descriptivo de ventas comerciales y visualización interactiva de datos.

**Institución:** IU Digital de Antioquia  
**Asignatura:** Analítica de Datos  
**Estudiante:** Sofia Miranda Cubides  
**Año:** 2026

## 1. Aplicación web

El proyecto cuenta con un dashboard interactivo desarrollado en Streamlit y desplegado en Streamlit Community Cloud.

**Acceso a la aplicación:** https://superkart-analytics.streamlit.app/

La aplicación permite consultar indicadores comerciales, explorar visualizaciones, aplicar filtros y descargar los resultados del análisis.

## Informe final del proyecto

El informe académico integra todas las etapas desarrolladas durante el semestre, incluyendo la necesidad analítica, el marco teórico, la metodología, el procesamiento de datos, las métricas, las visualizaciones, los resultados y las conclusiones.

- [Informe final en PDF](documento/Informe_Final_SuperKart.pdf)
- [Informe final en Word](documento/Informe_Final_SuperKart.docx)
- [Documento inicial del proyecto](documento/Proyecto_Integrador_EA2_Documento_Inicial.docx)

## 2. Descripción del proyecto

SuperKart Analytics surge como una propuesta para analizar el comportamiento de las ventas comerciales a partir de un conjunto de datos disponible en Hugging Face.

El proyecto integra las diferentes etapas desarrolladas durante la asignatura: identificación de una necesidad analítica, exploración de datos, limpieza, transformación, enriquecimiento, construcción de métricas, visualización y desarrollo de una aplicación web interactiva.

Su propósito es transformar los datos disponibles en información que facilite la comprensión del comportamiento comercial y sirva como apoyo para la toma de decisiones.

## 3. Necesidad analítica

En un escenario empresarial hipotético, una organización comercial necesita conocer cómo se distribuyen sus ventas entre las diferentes categorías de productos, establecimientos y ubicaciones.

El análisis busca identificar diferencias entre estos grupos y reconocer patrones comerciales que puedan orientar futuras decisiones relacionadas con el surtido de productos, la gestión de establecimientos y la evaluación de segmentos de precios.

## 4. Objetivo general

Analizar descriptivamente las ventas registradas en el dataset SuperKart mediante técnicas de procesamiento, transformación y visualización de datos, desarrollando una aplicación interactiva que facilite la interpretación de los resultados.

## 5. Dataset utilizado

| Característica | Descripción |
|---|---|
| Dataset | SuperKart Sales Dataset |
| Identificador | dev02chandan/sales-forecast-dataset |
| Plataforma | Hugging Face |
| Split utilizado | train |
| Registros originales | 7.414 |
| Variables originales | 12 |
| Variables después del enriquecimiento | 15 |
| Productos únicos | 7.414 |
| Establecimientos | 3 |
| Categorías de productos | 16 |
| Valores nulos | 0 |
| Registros duplicados | 0 |

**Fuente:** https://huggingface.co/datasets/dev02chandan/sales-forecast-dataset

Se utiliza el conjunto completo del split train, sin aplicar técnicas de muestreo. El split test no forma parte del análisis.

Cada registro se interpreta como una observación asociada a un producto y un establecimiento, no necesariamente como una transacción individual.

## 6. Preguntas de negocio

El análisis se desarrolla a partir de seis preguntas:

1. ¿Qué categorías de productos presentan mayores ventas totales y promedio?
2. ¿Qué diferencias se observan en las ventas de los establecimientos?
3. ¿Cómo se distribuyen las ventas según el tipo de ubicación?
4. ¿Qué relación existe entre el precio de los productos y las ventas registradas?
5. ¿Cómo se comportan las ventas según la clasificación del contenido de azúcar?
6. ¿Qué diferencias comerciales se observan entre los segmentos de precios?

Cada pregunta cuenta con métricas, visualizaciones e interpretaciones que permiten comprender los resultados y sus posibles aplicaciones comerciales.

## 7. Metodología

### 7.1. Exploración de datos

Se realizó la carga del dataset desde Hugging Face y su conversión a un DataFrame de Pandas.

Posteriormente, se revisaron las dimensiones, tipos de datos, valores nulos, categorías y características generales de las variables.

### 7.2. Limpieza y transformación

Durante esta etapa se realizaron las siguientes actividades:

- Verificación de registros duplicados.
- Identificación de valores nulos.
- Validación de variables numéricas.
- Revisión de valores negativos y valores en cero.
- Verificación de identificadores de productos y establecimientos.
- Normalización de la categoría reg a Regular en la variable Product_Sugar_Content.

La normalización permitió corregir una inconsistencia en 88 registros sin eliminar información.

El conjunto de datos conservó sus 7.414 observaciones originales.

### 7.3. Enriquecimiento de datos

Se incorporaron tres variables derivadas:

| Variable | Descripción |
|---|---|
| Sales_Range | Clasificación de las ventas en cuatro rangos mediante cuartiles. |
| Price_Range | Clasificación de los precios en cuatro segmentos mediante cuartiles. |
| Sales_Participation_Pct | Participación porcentual de cada observación respecto al total de ventas del dataset. |

Los rangos definidos fueron Bajo, Medio, Alto y Muy alto.

La segmentación mediante cuartiles permite comparar grupos con cantidades similares de observaciones, sin establecer límites de manera arbitraria.

El resultado se almacena en datos/datos_procesados.csv.

### 7.4. Construcción de métricas

| Métrica | Cálculo | Unidad |
|---|---|---|
| Ventas totales | Suma de Product_Store_Sales_Total | Unidades monetarias |
| Ventas promedio | Ventas totales / número de observaciones | Unidades monetarias por observación |
| Mediana | Valor central de las ventas ordenadas | Unidades monetarias |
| Participación | Ventas del grupo / ventas totales del universo analizado × 100 | Porcentaje |
| Productos únicos | Conteo de identificadores distintos | Productos |
| Establecimientos únicos | Conteo de identificadores distintos | Establecimientos |
| Correlación de Pearson | Asociación lineal entre precio y ventas | Coeficiente sin unidad |
| Correlación de Spearman | Asociación entre los rangos de precio y ventas | Coeficiente sin unidad |
| Distribución por segmentos | Observaciones de cada combinación / observaciones del segmento de precio × 100 | Porcentaje |

Debido a que la fuente no especifica la moneda, los valores se expresan en unidades monetarias (u. m.).

### 7.5. Visualización

Se utilizaron gráficas de barras, diagramas de participación, diagramas de dispersión y mapas de calor para representar los resultados.

Las visualizaciones fueron desarrolladas con Plotly y se encuentran disponibles tanto en el notebook como en la aplicación web.

### 7.6. Validación

Se realizaron comprobaciones para garantizar que las agrupaciones conservaran las ventas totales y la cantidad de observaciones, y que las participaciones porcentuales fueran consistentes.

También se verificó la coincidencia de los indicadores generales y las correlaciones entre el análisis y los módulos utilizados por la aplicación.

## 8. Principales resultados

### Indicadores generales

| Indicador | Resultado |
|---|---:|
| Ventas totales registradas | 23.681.606,33 u. m. |
| Ventas promedio por observación | 3.194,17 u. m. |
| Mediana de ventas | 3.255,06 u. m. |
| Productos únicos | 7.414 |
| Establecimientos | 3 |
| Categorías de productos | 16 |

### Categorías de productos

Fruits and Vegetables presenta las mayores ventas totales, con una participación del 14,37 %.

Starchy Foods registra el mayor promedio de ventas por observación, con 3.320,67 u. m.

Las tres categorías con mayores ventas concentran el 36,68 % del total registrado.

### Establecimientos

Supermarket Type2 concentra el 65,15 % de las ventas totales, mientras que Supermarket Type1 presenta el mayor promedio por observación, con 3.923,78 u. m.

Esta diferencia demuestra la importancia de analizar conjuntamente los valores acumulados y los promedios.

### Ubicaciones

Tier 2 concentra el 91,42 % de las ventas registradas. Sin embargo, cuenta con dos establecimientos, mientras que Tier 3 cuenta con uno.

Por esta razón, la comparación debe considerar la distribución de los registros y no atribuir las diferencias exclusivamente a la ubicación.

### Relación entre precio y ventas

Se obtuvo una correlación de Pearson de 0,7698 y una correlación de Spearman de 0,7854.

Los resultados indican una asociación positiva entre el precio y el valor de ventas registrado, pero no permiten establecer una relación causal.

### Contenido de azúcar

Low Sugar concentra el 55,39 % de las ventas totales, mientras que Regular presenta el mayor promedio por observación.

Las diferencias en el número de registros deben considerarse al interpretar estos resultados.

### Segmentos de precios

El segmento Muy alto concentra el 31,46 % de las ventas y presenta un promedio de 4.018,03 u. m. por observación.

Este comportamiento describe los datos disponibles, pero no demuestra que incrementar los precios genere mayores ventas.

## 9. Aplicación Streamlit

SuperKart Analytics cuenta con nueve secciones:

- Resumen ejecutivo.
- Productos.
- Establecimientos.
- Ubicaciones.
- Precio y ventas.
- Contenido de azúcar.
- Segmentos de precios.
- Conclusiones.
- Datos y metodología.

La aplicación incorpora filtros globales, indicadores dinámicos, visualizaciones interactivas, tablas de resultados y opciones de descarga.

Los cálculos se realizan a partir del archivo de datos procesados, utilizando módulos independientes para la carga de información, las métricas y las visualizaciones.

## 10. Tecnologías utilizadas

- Python 3.11
- Pandas
- NumPy
- Hugging Face Datasets
- Jupyter Notebook
- Plotly
- Matplotlib
- Streamlit
- Git y GitHub
- Visual Studio Code
- Streamlit Community Cloud

## 11. Estructura del proyecto

    Proyecto-Integrador-EA2/
    ├── .streamlit/
    │   └── config.toml
    ├── datos/
    │   └── datos_procesados.csv
    ├── documento/
    │   └── Proyecto_Integrador_EA2_Documento_Inicial.docx
    ├── notebooks/
    │   ├── exploracion_ventas.ipynb
    │   ├── transformacion_ventas.ipynb
    │   └── metricas_visualizaciones.ipynb
    ├── resultados/
    │   ├── graficas/
    │   ├── indicadores_generales.csv
    │   ├── validacion_metricas.csv
    │   └── demás resultados del análisis
    ├── src/
    │   ├── __init__.py
    │   ├── carga_datos.py
    │   ├── metricas.py
    │   └── visualizaciones.py
    ├── app.py
    ├── requirements.txt
    └── README.md

## 12. Instalación y ejecución local

### Clonar el repositorio

    git clone https://github.com/Sofimicu0105/Analitica-de-Datos.git
    cd Analitica-de-Datos/Proyecto-Integrador-EA2

### Crear un entorno virtual

    python -m venv .venv

### Activar el entorno virtual en Windows

    .venv\Scripts\Activate.ps1

### Instalar las dependencias

    python -m pip install -r requirements.txt

### Ejecutar la aplicación

    python -m streamlit run app.py

La aplicación estará disponible en la dirección local indicada por Streamlit en la terminal.

El archivo de datos procesados se encuentra incluido en el repositorio, por lo que no es necesario descargar nuevamente el dataset para ejecutar el dashboard.

## 13. Reproducción del análisis

Para reproducir el proceso completo, se deben abrir y ejecutar los notebooks en el siguiente orden:

1. notebooks/exploracion_ventas.ipynb
2. notebooks/transformacion_ventas.ipynb
3. notebooks/metricas_visualizaciones.ipynb

Se debe seleccionar el entorno virtual correspondiente y ejecutar las celdas en orden.

La descarga inicial desde Hugging Face requiere conexión a Internet.

Los archivos generados se almacenan en las carpetas datos y resultados. Las visualizaciones interactivas se encuentran en resultados/graficas.

## 14. Conclusiones y recomendaciones

El análisis permitió identificar diferencias en las ventas registradas según las categorías de productos, establecimientos, ubicaciones y segmentos de precios.

Los resultados muestran que una mayor participación en las ventas totales no implica necesariamente un mayor promedio por observación.

Se recomienda:

- Analizar conjuntamente las ventas totales, los promedios y la cantidad de observaciones.
- Revisar las categorías con mayor participación como punto de partida para estudios de surtido.
- Investigar las diferencias entre establecimientos considerando sus características particulares.
- Complementar el análisis con información sobre costos, cantidades vendidas, inventarios y fechas.
- Evaluar los segmentos de precios mediante estudios adicionales antes de realizar modificaciones comerciales.

## 15. Limitaciones

- El dataset no especifica la moneda utilizada.
- No se dispone de fechas de venta ni de un periodo comercial definido.
- El año de establecimiento no corresponde a la fecha de venta.
- Solo se analizan tres establecimientos.
- Cada tipo de establecimiento está representado por un único establecimiento.
- No se dispone de costos ni márgenes de ganancia, por lo que no es posible calcular rentabilidad.
- Las correlaciones no demuestran causalidad.
- No se ha confirmado si los datos corresponden a operaciones comerciales reales o sintéticas.
- No se ha verificado la licencia específica del dataset.
- Los resultados no deben generalizarse a otros establecimientos o mercados sin información adicional.

El proyecto tiene un alcance descriptivo y no incluye modelos predictivos.

## 16. Referencias

- Hugging Face. Dataset SuperKart. https://huggingface.co/datasets/dev02chandan/sales-forecast-dataset
- Hugging Face. Datasets Documentation. https://huggingface.co/docs/datasets/
- Python. Documentation. https://docs.python.org/3/
- Pandas. Documentation. https://pandas.pydata.org/docs/
- NumPy. Documentation. https://numpy.org/doc/
- Plotly. Python Documentation. https://plotly.com/python/
- Streamlit. Documentation. https://docs.streamlit.io/

---

Proyecto académico desarrollado para la asignatura Analítica de Datos de la IU Digital de Antioquia, 2026.