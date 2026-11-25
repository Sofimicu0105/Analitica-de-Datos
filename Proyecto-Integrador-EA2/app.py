import streamlit as st
import pandas as pd
import numpy as np

from src.carga_datos import cargar_datos

from src.metricas import (
    calcular_indicadores,
    calcular_metricas,
    calcular_correlaciones,
    correlaciones_por_establecimiento,
    calcular_cruce_segmentos,
    filtrar_datos,
    COL_VENTAS,
    ORDEN_RANGOS
)

from src.visualizaciones import (
    grafico_ventas,
    grafico_promedio,
    grafico_participacion,
    grafico_correlacion,
    grafico_mapa_calor,
    COLORES_TIENDAS,
    COLORES_AZUCAR
)


st.set_page_config(
    page_title="SuperKart Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 2rem;
        max-width: 1600px;
    }

    [data-testid="stMetric"] {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 18px;
        min-height: 125px;
    }

    [data-testid="stMetricValue"] {
        color: #5EEAD4;
        font-size: 28px;
    }

    [data-testid="stSidebar"] {
        border-right: 1px solid #334155;
    }

    .marca {
        font-size: 30px;
        font-weight: 800;
        color: #14B8A6;
        letter-spacing: -1px;
    }

    .submarca {
        font-size: 12px;
        color: #94A3B8;
        letter-spacing: 3px;
    }

    .encabezado {
        color: #94A3B8;
        font-size: 15px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)


df_original = cargar_datos()


def formato(valor, decimales=2):
    if pd.isna(valor):
        return "No disponible"

    return f"{valor:,.{decimales}f}".translate(
        str.maketrans(",.", ".,")
    )


def mostrar_grafica(fig):
    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displaylogo": False}
    )


def mostrar_tabla(tabla):
    st.dataframe(
        tabla.round(2),
        use_container_width=True,
        hide_index=True
    )


def descargar_tabla(tabla, nombre):
    st.download_button(
        label="Descargar resultados CSV",
        data=tabla.to_csv(index=False).encode("utf-8-sig"),
        file_name=f"{nombre}.csv",
        mime="text/csv"
    )


def encabezado(titulo, descripcion):
    st.title(titulo)
    st.markdown(
        f'<div class="encabezado">{descripcion}</div>',
        unsafe_allow_html=True
    )


def mostrar_indicadores(datos):
    indicadores = calcular_indicadores(datos)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Ventas totales",
        formato(indicadores["ventas_totales"]),
        help="Suma de ventas registradas en unidades monetarias."
    )

    c2.metric(
        "Ventas promedio",
        formato(indicadores["ventas_promedio"]),
        help="Unidades monetarias por observación."
    )

    c3.metric(
        "Productos únicos",
        formato(indicadores["productos"], 0)
    )

    c4.metric(
        "Establecimientos",
        indicadores["establecimientos"]
    )


def mostrar_metricas_metodologia():
    with st.expander("Definición y cálculo de las métricas"):
        st.markdown("""
        - **Ventas totales:** suma de Product_Store_Sales_Total.
          Unidad: unidades monetarias (u. m.).
        - **Ventas promedio:** ventas totales divididas entre
          el número de observaciones.
          Unidad: u. m. por observación.
        - **Participación:** ventas del grupo divididas entre
          las ventas del conjunto seleccionado, multiplicadas
          por 100. Unidad: porcentaje.
        - **Observaciones:** cantidad de registros del grupo.
        - **Periodo:** no especificado en el dataset.
        """)


def mostrar_analisis(tabla, columna, recomendacion, limitacion):
    lider_total = tabla.loc[
        tabla["Ventas_totales"].idxmax()
    ]

    lider_promedio = tabla.loc[
        tabla["Ventas_promedio"].idxmax()
    ]

    st.subheader("Interpretación de resultados")

    st.markdown(
        f"**{lider_total[columna]}** concentra la mayor "
        f"participación en las ventas seleccionadas, con "
        f"**{formato(lider_total['Participacion_pct'])} %** "
        f"y {formato(lider_total['Ventas_totales'])} u. m."
    )

    st.markdown(
        f"El mayor promedio por observación corresponde a "
        f"**{lider_promedio[columna]}**, con "
        f"**{formato(lider_promedio['Ventas_promedio'])} u. m.**"
    )

    st.subheader("Recomendación comercial")
    st.write(recomendacion)

    st.subheader("Limitaciones")
    st.write(limitacion)


# Navegación y filtros

with st.sidebar:

    st.markdown(
        '<div class="marca">SuperKart</div>'
        '<div class="submarca">ANALYTICS</div>',
        unsafe_allow_html=True
    )

    st.divider()

    pagina = st.radio(
        "NAVEGACIÓN",
        [
            "Resumen ejecutivo",
            "Productos",
            "Establecimientos",
            "Ubicaciones",
            "Precio y ventas",
            "Contenido de azúcar",
            "Segmentos de precios",
            "Conclusiones",
            "Datos y metodología"
        ]
    )

    st.divider()
    st.markdown("**FILTROS GLOBALES**")

    opciones_filtros = {
        "Product_Type": sorted(
            df_original["Product_Type"].unique()
        ),
        "Store_Type": sorted(
            df_original["Store_Type"].unique()
        ),
        "Store_Location_City_Type": sorted(
            df_original["Store_Location_City_Type"].unique()
        ),
        "Product_Sugar_Content": sorted(
            df_original["Product_Sugar_Content"].unique()
        ),
        "Price_Range": ORDEN_RANGOS
    }

    etiquetas = {
        "Product_Type": "Categoría de producto",
        "Store_Type": "Establecimiento",
        "Store_Location_City_Type": "Ubicación",
        "Product_Sugar_Content": "Contenido de azúcar",
        "Price_Range": "Segmento de precios"
    }

    if st.button(
        "Restablecer filtros",
        use_container_width=True
    ):
        for columna, opciones in opciones_filtros.items():
            st.session_state[f"filtro_{columna}"] = opciones

    filtros = {}

    for columna, opciones in opciones_filtros.items():

        filtros[columna] = st.multiselect(
            etiquetas[columna],
            options=opciones,
            default=opciones,
            key=f"filtro_{columna}"
        )

    st.divider()
    st.caption("Proyecto integrador · 2026")
    st.caption("IU Digital de Antioquia")


df = filtrar_datos(df_original, filtros)

st.caption(
    f"Registros seleccionados: {formato(len(df), 0)} "
    f"de {formato(len(df_original), 0)} | "
    "Periodo de ventas no especificado"
)

if df.empty:
    st.warning(
        "No existen registros para la combinación de filtros "
        "seleccionada. Modifica o restablece los filtros."
    )
    st.stop()


# Resumen ejecutivo

if pagina == "Resumen ejecutivo":

    encabezado(
        "SuperKart Analytics",
        "Inteligencia comercial y análisis descriptivo de ventas"
    )

    mostrar_indicadores(df)

    st.divider()

    st.subheader("Panorama comercial")

    categorias = calcular_metricas(df, "Product_Type")
    tiendas = calcular_metricas(df, "Store_Type")

    c1, c2 = st.columns([1.2, 1])

    with c1:
        mostrar_grafica(
            grafico_ventas(
                categorias.head(8),
                "Product_Type",
                "Principales categorías por ventas",
                "Categoría"
            )
        )

    with c2:
        mostrar_grafica(
            grafico_participacion(
                tiendas,
                "Store_Type",
                "Participación por establecimiento",
                COLORES_TIENDAS
            )
        )

    st.subheader("Hallazgos principales")

    lider_categoria = categorias.iloc[0]
    lider_tienda = tiendas.iloc[0]

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.caption("Categoría líder")
            st.subheader(lider_categoria["Product_Type"])
            st.write(
                f"{formato(lider_categoria['Participacion_pct'])} % "
                "de las ventas seleccionadas."
            )

    with c2:
        with st.container(border=True):
            st.caption("Establecimiento líder")
            st.subheader(lider_tienda["Store_Type"])
            st.write(
                f"{formato(lider_tienda['Participacion_pct'])} % "
                "de participación."
            )

    with c3:
        with st.container(border=True):
            st.caption("Mediana de ventas")
            st.subheader(formato(df[COL_VENTAS].median()))
            st.write("Unidades monetarias por observación.")

    st.subheader("Necesidad de negocio")

    st.write("""
    Identificar cómo se distribuyen las ventas registradas
    entre las categorías de productos y establecimientos,
    con el propósito de apoyar la revisión del portafolio
    y las decisiones comerciales.
    """)

    st.caption(
        "Fuente: SuperKart, split train del dataset "
        "dev02chandan/sales-forecast-dataset."
    )


# Pregunta 1

elif pagina == "Productos":

    encabezado(
        "Análisis de productos",
        "¿Qué categorías concentran las mayores ventas registradas?"
    )

    mostrar_indicadores(df)
    mostrar_metricas_metodologia()

    tabla = calcular_metricas(df, "Product_Type")

    tab1, tab2, tab3 = st.tabs([
        "Ventas totales",
        "Ventas promedio",
        "Detalle de resultados"
    ])

    with tab1:
        mostrar_grafica(
            grafico_ventas(
                tabla,
                "Product_Type",
                "Ventas registradas por categoría",
                "Categoría de producto"
            )
        )

    with tab2:
        mostrar_grafica(
            grafico_promedio(
                tabla,
                "Product_Type",
                "Ventas promedio por categoría",
                "Categoría de producto"
            )
        )

    with tab3:
        mostrar_tabla(tabla)
        descargar_tabla(tabla, "ventas_por_categoria")

    mostrar_analisis(
        tabla,
        "Product_Type",
        "Revisar la composición del portafolio y priorizar "
        "el seguimiento de las categorías con mayor "
        "participación comercial.",
        "Las categorías tienen diferentes cantidades de "
        "observaciones. Las ventas acumuladas no representan "
        "necesariamente rentabilidad ni demanda."
    )


# Pregunta 2

elif pagina == "Establecimientos":

    encabezado(
        "Análisis de establecimientos",
        "¿Qué diferencias comerciales existen entre las tiendas?"
    )

    mostrar_indicadores(df)
    mostrar_metricas_metodologia()

    tabla = calcular_metricas(df, "Store_Type")

    c1, c2 = st.columns(2)

    with c1:
        mostrar_grafica(
            grafico_ventas(
                tabla,
                "Store_Type",
                "Ventas totales por establecimiento",
                "Establecimiento"
            )
        )

    with c2:
        mostrar_grafica(
            grafico_promedio(
                tabla,
                "Store_Type",
                "Ventas promedio por establecimiento",
                "Establecimiento"
            )
        )

    mostrar_tabla(tabla)
    descargar_tabla(tabla, "ventas_por_establecimiento")

    mostrar_analisis(
        tabla,
        "Store_Type",
        "Comparar los portafolios y las condiciones comerciales "
        "de las tiendas antes de definir estrategias de mejora.",
        "Cada formato comercial está representado por una "
        "única tienda. No es posible atribuir las diferencias "
        "exclusivamente al tipo de establecimiento."
    )


# Pregunta 3

elif pagina == "Ubicaciones":

    encabezado(
        "Análisis de ubicaciones",
        "¿Cómo se distribuyen las ventas según el tipo de ubicación?"
    )

    mostrar_indicadores(df)
    mostrar_metricas_metodologia()

    columna = "Store_Location_City_Type"

    tabla = calcular_metricas(df, columna)

    cantidad_tiendas = df.groupby(columna)["Store_Id"].nunique()

    tabla["Establecimientos"] = tabla[columna].map(
        cantidad_tiendas
    )

    c1, c2 = st.columns(2)

    with c1:
        mostrar_grafica(
            grafico_participacion(
                tabla,
                columna,
                "Participación por ubicación",
                {
                    "Tier 2": "#14B8A6",
                    "Tier 3": "#6366F1"
                }
            )
        )

    with c2:
        mostrar_grafica(
            grafico_promedio(
                tabla,
                columna,
                "Ventas promedio por ubicación",
                "Tipo de ubicación"
            )
        )

    mostrar_tabla(tabla)
    descargar_tabla(tabla, "ventas_por_ubicacion")

    mostrar_analisis(
        tabla,
        columna,
        "Revisar las condiciones comerciales y el portafolio "
        "de los establecimientos por ubicación.",
        "El dataset no identifica ciudades específicas. "
        "Las ubicaciones tienen diferente número de tiendas "
        "y no se puede establecer una relación causal."
    )


# Pregunta 4

elif pagina == "Precio y ventas":

    encabezado(
        "Relación entre precio y ventas",
        "¿Existe una asociación entre el precio y el valor de ventas?"
    )

    correlaciones = calcular_correlaciones(df)

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Pearson",
        formato(correlaciones["Pearson"], 4)
    )

    c2.metric(
        "Spearman",
        formato(correlaciones["Spearman"], 4)
    )

    c3.metric(
        "Observaciones",
        formato(len(df), 0)
    )

    with st.expander("Definición y cálculo de las métricas"):
        st.markdown("""
        **Pearson:** covarianza entre precio y ventas dividida
        entre el producto de sus desviaciones estándar.

        **Spearman:** correlación de Pearson aplicada sobre
        los rangos de ambas variables.

        Ambos coeficientes son adimensionales y se encuentran
        entre -1 y 1. No representan porcentajes ni causalidad.
        """)

    mostrar_grafica(grafico_correlacion(df))

    st.subheader("Correlación por establecimiento")

    tabla = correlaciones_por_establecimiento(df)

    mostrar_tabla(tabla)
    descargar_tabla(tabla, "correlacion_establecimientos")

    st.subheader("Interpretación de resultados")

    pearson = correlaciones["Pearson"]

    if pd.isna(pearson):
        st.write(
            "No hay suficiente variabilidad o cantidad de "
            "registros para calcular la correlación."
        )

    else:
        magnitud = abs(pearson)

        if magnitud >= 0.7:
            intensidad = "fuerte"
        elif magnitud >= 0.4:
            intensidad = "moderada"
        else:
            intensidad = "débil"

        direccion = "positiva" if pearson > 0 else "negativa"

        if pearson == 0:
            st.write("No se observa asociación lineal.")
        else:
            st.write(
                f"Los registros seleccionados presentan una "
                f"asociación lineal {direccion} {intensidad}, "
                f"con un coeficiente de {formato(pearson, 4)}."
            )

    st.caption(
        "La clasificación de intensidad utiliza umbrales "
        "descriptivos orientativos."
    )

    st.subheader("Recomendación comercial")

    st.write(
        "Evaluar las estrategias de precios de forma diferenciada "
        "por establecimiento y complementar el análisis con "
        "cantidades vendidas, costos y promociones."
    )

    st.subheader("Limitaciones")

    st.write(
        "La correlación no implica causalidad. Los resultados "
        "no permiten estimar la elasticidad de la demanda "
        "ni afirmar que aumentar los precios genere mayores ventas."
    )


# Pregunta 5

elif pagina == "Contenido de azúcar":

    encabezado(
        "Contenido de azúcar",
        "¿Qué diferencias comerciales existen entre las clasificaciones?"
    )

    mostrar_indicadores(df)
    mostrar_metricas_metodologia()

    columna = "Product_Sugar_Content"

    tabla = calcular_metricas(df, columna)

    c1, c2 = st.columns(2)

    with c1:
        mostrar_grafica(
            grafico_participacion(
                tabla,
                columna,
                "Participación según contenido de azúcar",
                COLORES_AZUCAR
            )
        )

    with c2:
        mostrar_grafica(
            grafico_promedio(
                tabla,
                columna,
                "Ventas promedio por clasificación",
                "Contenido de azúcar"
            )
        )

    mostrar_tabla(tabla)
    descargar_tabla(tabla, "ventas_por_azucar")

    mostrar_analisis(
        tabla,
        columna,
        "Revisar la distribución del portafolio según las "
        "clasificaciones de contenido de azúcar.",
        "No se dispone de información sobre hábitos de consumo "
        "ni cantidades vendidas. La participación comercial "
        "no demuestra preferencias individuales de compra."
    )


# Pregunta 6

elif pagina == "Segmentos de precios":

    encabezado(
        "Segmentos de precios",
        "¿Qué segmentos concentran las mayores ventas registradas?"
    )

    mostrar_indicadores(df)
    mostrar_metricas_metodologia()

    tabla = calcular_metricas(df, "Price_Range")

    tabla["Price_Range"] = pd.Categorical(
        tabla["Price_Range"],
        categories=ORDEN_RANGOS,
        ordered=True
    )

    tabla = tabla.sort_values("Price_Range")

    c1, c2 = st.columns(2)

    with c1:
        mostrar_grafica(
            grafico_ventas(
                tabla,
                "Price_Range",
                "Ventas totales por segmento",
                "Segmento de precios"
            )
        )

    with c2:
        mostrar_grafica(
            grafico_promedio(
                tabla,
                "Price_Range",
                "Ventas promedio por segmento",
                "Segmento de precios"
            )
        )

    st.subheader("Cruce entre rangos de precios y ventas")

    cruce = calcular_cruce_segmentos(df)

    mostrar_grafica(grafico_mapa_calor(cruce))

    st.caption(
        "Cada fila con observaciones representa el 100 % "
        "del segmento de precios. Las filas sin registros "
        "se muestran en cero."
    )

    mostrar_tabla(tabla)
    descargar_tabla(tabla, "ventas_por_segmento")

    mostrar_analisis(
        tabla,
        "Price_Range",
        "Identificar los segmentos con mayor participación "
        "para orientar la revisión del portafolio y las "
        "estrategias de precios.",
        "Los segmentos se definieron mediante cuartiles del "
        "dataset original. Mayores ventas monetarias no "
        "implican mayor rentabilidad ni más unidades vendidas."
    )


# Conclusiones generales

elif pagina == "Conclusiones":

    encabezado(
        "Conclusiones y recomendaciones",
        "Principales resultados del análisis comercial"
    )

    st.info(
        "Esta sección presenta las conclusiones del dataset "
        "completo, independientemente de los filtros activos."
    )

    st.subheader("Principales hallazgos")

    hallazgos = [
        (
            "Categorías de productos",
            "Fruits and Vegetables concentra el 14,37 % de "
            "las ventas, mientras que Starchy Foods presenta "
            "el mayor promedio por observación."
        ),
        (
            "Establecimientos",
            "Supermarket Type2 concentra el 65,15 % de las "
            "ventas. Supermarket Type1 registra el mayor "
            "promedio, con 3.923,78 u. m."
        ),
        (
            "Ubicaciones",
            "Tier 2 concentra el 91,42 % de las ventas "
            "registradas."
        ),
        (
            "Precio y ventas",
            "Pearson de 0,7698 y Spearman de 0,7854 indican "
            "una asociación positiva entre precio y ventas."
        ),
        (
            "Contenido de azúcar",
            "Low Sugar concentra el 55,39 % de las ventas, "
            "aunque los promedios de las clasificaciones "
            "son similares."
        ),
        (
            "Segmentos de precios",
            "Los segmentos alto y muy alto concentran "
            "aproximadamente el 58,64 % de las ventas."
        )
    ]

    for titulo, contenido in hallazgos:
        with st.container(border=True):
            st.markdown(f"**{titulo}**")
            st.write(contenido)

    st.subheader("Recomendaciones comerciales")

    st.markdown("""
    - Priorizar el seguimiento de las categorías con mayor
      participación en las ventas.
    - Comparar los portafolios de los establecimientos.
    - Evaluar las estrategias de precios de manera diferenciada.
    - Complementar el análisis con costos, inventarios,
      cantidades vendidas y periodos comerciales.
    """)

    st.subheader("Limitaciones generales")

    st.markdown("""
    - No se conoce la moneda ni el periodo de ventas.
    - Solo se analizaron tres establecimientos.
    - No se dispone de costos ni márgenes de utilidad.
    - No se conocen las cantidades vendidas.
    - No se ha verificado si los datos son reales o sintéticos.
    - Los resultados son descriptivos y no causales.
    """)


# Datos y metodología

elif pagina == "Datos y metodología":

    encabezado(
        "Datos y metodología",
        "Fuente, preparación, calidad y reproducibilidad"
    )

    st.subheader("Identificación del dataset")

    st.markdown("""
    **Nombre:** SuperKart Sales Forecast Dataset

    **Identificador:** `dev02chandan/sales-forecast-dataset`

    **Fuente:** [Hugging Face](https://huggingface.co/datasets/dev02chandan/sales-forecast-dataset)

    **Partición utilizada:** train

    **Unidad de análisis:** registro asociado a un producto
    y establecimiento.
    """)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Registros", len(df_original))
    c2.metric("Variables originales", 12)
    c3.metric("Variables finales", df_original.shape[1])
    c4.metric("Valores nulos", int(df_original.isna().sum().sum()))

    st.subheader("Metodología")

    st.markdown("""
    1. Carga y exploración del dataset.
    2. Diagnóstico de calidad y validación de variables.
    3. Normalización de categorías de contenido de azúcar.
    4. Enriquecimiento mediante variables derivadas.
    5. Cálculo de métricas y análisis descriptivo.
    6. Construcción de visualizaciones interactivas.
    7. Validación de resultados y desarrollo del dashboard.
    """)

    st.subheader("Transformaciones realizadas")

    transformaciones = pd.DataFrame({
        "Transformación": [
            "Normalización de azúcar",
            "Sales_Range",
            "Price_Range",
            "Sales_Participation_Pct"
        ],
        "Descripción": [
            "Unificación de reg y Regular",
            "Clasificación de ventas mediante cuartiles",
            "Clasificación de precios mediante cuartiles",
            "Participación individual sobre las ventas originales"
        ]
    })

    mostrar_tabla(transformaciones)

    st.subheader("Consulta de datos")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=450
    )

    descargar_tabla(df, "superkart_datos_filtrados")

    st.caption(
        "Sales_Participation_Pct conserva su cálculo sobre "
        "el dataset completo. Las participaciones de las "
        "gráficas se recalculan sobre los filtros activos."
    )

    st.subheader("Tecnologías utilizadas")

    st.write(
        "Python · Pandas · NumPy · Hugging Face · "
        "Plotly · Streamlit · Git · GitHub"
    )


st.divider()

st.caption(
    "SuperKart Analytics | Proyecto integrador de Analítica "
    "de Datos | IU Digital de Antioquia | 2026"
)