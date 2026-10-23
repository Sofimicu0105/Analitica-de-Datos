# Actividad 1 - Analítica de Datos

## 📝 Documentación de la Primera Entrega
En esta primera etapa del proyecto, nos enfocamos en establecer la estructura base y la conexión con las fuentes de datos. Los puntos clave realizados fueron:
- **Conexión con la Plataforma:** Se configuró el entorno para conectar el proyecto con el repositorio de **Hugging Face**.
- **Carga de Datos:** Se importó con éxito el conjunto de datos de flores (**Iris Dataset**).
- **Módulos de Código:** Se implementaron y validaron las clases locales `hf_dataset_loader.py` (para la descarga) y `dataset_summarizer.py` (para obtener el resumen inicial de las filas y columnas).
- **Control de Versiones:** Se gestionó la configuración mediante Git utilizando ramas de características individuales para trabajar de forma colaborativa y ordenada.

---

## 🚀 Consulta Analítica Adicional (Google Colab)
Para profundizar en el análisis exploratorio de los datos y experimentar sin restricciones en la nube, se trasladó el flujo a **Google Colab**. Se diseñó una consulta analítica orientada a entender las características morfológicas del dataset:

### Objetivos de la Consulta:
1. Analizar la distribución y relaciones de las variables del dataset *Iris*.
2. Verificar comportamientos o métricas clave sobre el tamaño de los sépalos y pétalos mediante operaciones directas en el DataFrame.

### Conclusiones del Análisis:
- El análisis en Colab permitió verificar de forma rápida la consistencia de los datos cargados desde Hugging Face.
- Se facilitó la visualización de las métricas principales (como promedios y conteos), asegurando que el dataset está limpio y listo para las fases de modelado o transformaciones avanzadas.