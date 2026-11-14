# Comparación de datos climáticos: Medellín y Madrid (2024)

## Introducción

En esta actividad se realiza una comparación de los datos climáticos de Medellín, Colombia, y Madrid, España, durante el año 2024. Para ello, se utilizan datos diarios de temperatura máxima y precipitación, obtenidos de Open-Meteo.

El análisis se desarrolla en Python utilizando Pandas para organizar y validar los datos, NumPy para realizar operaciones numéricas y Matplotlib para representar los resultados mediante gráficas.

## Objetivo

Comparar el comportamiento de las temperaturas máximas diarias y las precipitaciones de Medellín y Madrid durante 2024, identificando similitudes y diferencias mediante estadísticas descriptivas y visualizaciones.

## Hipótesis

Antes de realizar el análisis, se plantea que Medellín tendrá temperaturas máximas diarias más estables durante el año, mientras que Madrid presentará mayores variaciones debido a las diferencias entre sus estaciones.

También se espera que Medellín registre una mayor cantidad de días con precipitación y un acumulado anual de lluvia superior al de Madrid.

Estas expectativas se contrastarán con los datos obtenidos para 2024.

## Fuente de los datos

Los datos utilizados en esta actividad fueron obtenidos de **Open-Meteo Historical Weather API**, utilizando el modelo de reanálisis climático **ERA5**.

Se seleccionaron dos ciudades:

- **Medellín, Colombia:** latitud 6.2442, longitud -75.5812.
- **Madrid, España:** latitud 40.4168, longitud -3.7038.

El periodo analizado comprende desde el **1 de enero hasta el 31 de diciembre de 2024**, con una frecuencia diaria de 366 registros por ciudad.

Las variables seleccionadas fueron:

- `time`: fecha del registro.
- `temperature_2m_max (°C)`: temperatura máxima diaria en grados Celsius.
- `precipitation_sum (mm)`: precipitación acumulada diaria en milímetros.

Se utilizó ERA5 porque permitió obtener registros completos de temperatura y precipitación para ambas ciudades. Los datos corresponden a un modelo de reanálisis, por lo que no representan mediciones directas de una estación meteorológica.

### Enlaces de consulta

- [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api)
- [Datos de Medellín](https://archive-api.open-meteo.com/v1/archive?latitude=6.2442&longitude=-75.5812&start_date=2024-01-01&end_date=2024-12-31&daily=temperature_2m_max,precipitation_sum&timezone=America%2FBogota&models=era5&format=csv)
- [Datos de Madrid](https://archive-api.open-meteo.com/v1/archive?latitude=40.4168&longitude=-3.7038&start_date=2024-01-01&end_date=2024-12-31&daily=temperature_2m_max,precipitation_sum&timezone=Europe%2FMadrid&models=era5&format=csv)

## Metodología

Para desarrollar la comparación climática se utilizaron Python y las librerías Pandas, NumPy y Matplotlib.

### 1. Carga de los datos

Se descargaron dos archivos CSV de Open-Meteo, uno para Medellín y otro para Madrid.

Los archivos se cargaron con `pd.read_csv()`, utilizando `skiprows=3` para omitir las líneas iniciales de información del modelo y comenzar la lectura desde los encabezados de las variables.

### 2. Validación de los datos

La columna `time` se convirtió al formato de fecha mediante `pd.to_datetime()` para facilitar las consultas y agrupaciones mensuales.

Después se verificaron la cantidad de registros, las fechas iniciales y finales, los valores faltantes y las fechas duplicadas.

Ambas ciudades presentaron 366 registros, sin valores faltantes ni fechas duplicadas. También se comprobó que las fechas coincidieran, permitiendo comparar el mismo periodo.

No fue necesario eliminar registros ni reemplazar valores.

### 3. Operaciones con NumPy

Las columnas de temperatura y precipitación se convirtieron en arrays mediante `.to_numpy()` para realizar operaciones numéricas.

Se utilizaron índices y slicing para consultar temperaturas de días específicos y seleccionar los primeros siete días del año.

También se aplicaron máscaras booleanas para identificar los días con precipitación superior a 0 mm y aquellos con temperatura máxima superior a 25 °C.

Con `np.mean()`, `np.min()`, `np.max()` y `np.sum()` se calcularon las estadísticas principales de cada ciudad.

Finalmente, se utilizó broadcasting para restar el promedio anual de temperatura máxima diaria a cada registro del array. Esto permitió identificar cuánto se alejaba cada día del promedio de su ciudad sin utilizar ciclos.

### 4. Agrupación mensual

Los datos se agruparon por mes mediante `groupby()`.

Para las temperaturas se utilizó `.mean()`, ya que se buscaba calcular el promedio mensual de las temperaturas máximas diarias.

Para las precipitaciones se utilizó `.sum()`, porque el objetivo era conocer la cantidad total de lluvia acumulada durante cada mes.

### 5. Visualización

Se elaboraron tres gráficas con Matplotlib:

- Una gráfica de líneas para comparar los promedios mensuales de temperatura máxima diaria.
- Una gráfica de barras agrupadas para comparar la precipitación acumulada por mes.
- Un histograma para observar la distribución de las temperaturas máximas diarias de ambas ciudades, utilizando los mismos intervalos.

Estas visualizaciones permitieron identificar diferencias en la variación de las temperaturas y en la distribución de las precipitaciones durante 2024.

## Análisis complementario

Para complementar la comparación climática, se calcularon los porcentajes de días con precipitación y de días con temperaturas máximas superiores a 25 °C durante 2024.

| Indicador | Medellín | Madrid |
|---|---:|---:|
| Días con precipitación | 93,44 % | 34,97 % |
| Días con temperatura máxima superior a 25 °C | 86,61 % | 33,88 % |

Los resultados muestran que Medellín registró precipitación durante una mayor proporción del año. Mientras que en Medellín hubo lluvia en aproximadamente 93 de cada 100 días, en Madrid se registró en cerca de 35 de cada 100 días.

También se encontró que Medellín presentó una mayor frecuencia de temperaturas máximas superiores a 25 °C. Sin embargo, esto no significa que haya alcanzado las temperaturas más altas del año, ya que Madrid registró una máxima de 39,80 °C, frente a los 32,20 °C de Medellín.

Estos resultados complementan las estadísticas y las gráficas del notebook principal.

Los porcentajes se calcularon mediante el archivo `analisis.py`, utilizando los mismos datos de Open-Meteo empleados en el proyecto.

## Instalación y ejecución

Para ejecutar este proyecto es necesario tener instalado Python y contar con acceso a Jupyter Notebook o Visual Studio Code.

### 1. Instalar las dependencias

Desde la carpeta `EA3_comparacion_climatica`, abrir una terminal y ejecutar:

```bash
python -m pip install -r requirements.txt
```

Este comando instala las librerías necesarias: Pandas, NumPy, Matplotlib, Jupyter e ipykernel.

### 2. Ejecutar el análisis principal

Abrir el archivo `EA3_Miranda_Sofia.ipynb` en Visual Studio Code o Jupyter Notebook.

Seleccionar un entorno de Python que tenga instaladas las dependencias y ejecutar todas las celdas en orden.

El notebook permite consultar la validación de los datos, los cálculos estadísticos y las tres gráficas comparativas.

### 3. Ejecutar el análisis complementario

Desde la carpeta `EA3_comparacion_climatica`, ejecutar:

```bash
python analisis.py
```

Este archivo calcula los porcentajes de días con precipitación y de días con temperaturas máximas superiores a 25 °C para ambas ciudades.

### 4. Archivos del proyecto

- `EA3_Miranda_Sofia.ipynb`: análisis principal y visualizaciones.
- `analisis.py`: análisis complementario de porcentajes.
- `datos/medellin.csv`: datos climáticos diarios de Medellín.
- `datos/madrid.csv`: datos climáticos diarios de Madrid.
- `requirements.txt`: dependencias necesarias.
- `README.md`: documentación del proyecto.

Los archivos CSV están incluidos en el repositorio, por lo que no es necesario descargarlos nuevamente para ejecutar los análisis.

## Limitaciones

El análisis utiliza información correspondiente únicamente al año 2024, por lo que sus resultados no representan necesariamente el comportamiento climático de otros años.

Los datos provienen del modelo de reanálisis ERA5 y no de mediciones directas realizadas en estaciones meteorológicas. Además, representan las condiciones estimadas para las ubicaciones geográficas consultadas, que pueden diferir de las condiciones particulares de otros sectores de cada ciudad.

Por último, se analizaron solamente dos variables: temperatura máxima diaria y precipitación. Otros factores, como humedad, viento y altitud, no se incluyeron en la comparación.