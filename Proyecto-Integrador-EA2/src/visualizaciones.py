import plotly.express as px
import plotly.graph_objects as go
import numpy as np

from src.metricas import COL_VENTAS, COL_PRECIO


TURQUESA = "#14B8A6"
VIOLETA = "#6366F1"
AMARILLO = "#F59E0B"
FONDO = "#0F172A"

PALETA = [
    TURQUESA,
    VIOLETA,
    AMARILLO,
    "#38BDF8",
    "#EC4899",
    "#84CC16"
]

COLORES_TIENDAS = {
    "Supermarket Type2": TURQUESA,
    "Supermarket Type1": VIOLETA,
    "Food Mart": AMARILLO
}

COLORES_AZUCAR = {
    "Low Sugar": TURQUESA,
    "Regular": VIOLETA,
    "No Sugar": AMARILLO
}


def aplicar_estilo(fig, altura=450):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=FONDO,
        plot_bgcolor=FONDO,
        font=dict(
            family="Arial",
            color="#F8FAFC",
            size=12
        ),
        height=altura,
        margin=dict(l=20, r=30, t=65, b=40),
        title_font_size=17,
        colorway=PALETA,
        hoverlabel=dict(
            bgcolor="#1E293B",
            font_color="#F8FAFC"
        )
    )

    fig.update_xaxes(gridcolor="#263449")
    fig.update_yaxes(gridcolor="#263449")

    return fig


def grafico_ventas(tabla, columna, titulo, etiqueta):
    datos = tabla.sort_values("Ventas_totales")

    fig = px.bar(
        datos,
        x="Ventas_totales",
        y=columna,
        orientation="h",
        text="Participacion_pct",
        title=titulo,
        color="Ventas_totales",
        color_continuous_scale=[
            "#1E3A5F",
            TURQUESA
        ],
        labels={
            columna: etiqueta,
            "Ventas_totales": "Ventas totales (u. m.)",
            "Participacion_pct": "Participación (%)"
        },
        hover_data={
            "Observaciones": True,
            "Ventas_promedio": ":,.2f"
        }
    )

    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
        cliponaxis=False
    )

    fig.update_layout(
        coloraxis_showscale=False,
        showlegend=False
    )

    fig.update_xaxes(
        range=[0, datos["Ventas_totales"].max() * 1.18]
    )

    return aplicar_estilo(
        fig, max(350, len(datos) * 30 + 130)
    )


def grafico_promedio(tabla, columna, titulo, etiqueta):
    datos = tabla.sort_values("Ventas_promedio")

    fig = px.bar(
        datos,
        x="Ventas_promedio",
        y=columna,
        orientation="h",
        text="Ventas_promedio",
        title=titulo,
        color_discrete_sequence=[VIOLETA],
        labels={
            columna: etiqueta,
            "Ventas_promedio": "Ventas promedio (u. m. por observación)"
        }
    )

    fig.update_traces(
        texttemplate="%{text:,.2f}",
        textposition="outside",
        cliponaxis=False
    )

    fig.update_xaxes(
        range=[0, datos["Ventas_promedio"].max() * 1.20]
    )

    return aplicar_estilo(
        fig, max(350, len(datos) * 30 + 130)
    )


def grafico_participacion(
    tabla, columna, titulo, colores=None
):
    fig = px.pie(
        tabla,
        names=columna,
        values="Ventas_totales",
        hole=0.65,
        title=titulo,
        color=columna,
        color_discrete_map=colores or {},
        color_discrete_sequence=PALETA
    )

    fig.update_traces(
        textinfo="label+percent",
        marker=dict(
            line=dict(color=FONDO, width=2)
        )
    )

    total = tabla["Ventas_totales"].sum()

    fig.add_annotation(
        text=f"{total / 1e6:.2f} M<br>u. m.",
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(size=20)
    )

    return aplicar_estilo(fig)


def grafico_correlacion(df):
    fig = px.scatter(
        df,
        x=COL_PRECIO,
        y=COL_VENTAS,
        color="Store_Type",
        opacity=0.45,
        title="Relación entre precio y ventas",
        color_discrete_map=COLORES_TIENDAS,
        labels={
            COL_PRECIO: "Precio registrado (u. m.)",
            COL_VENTAS: "Ventas registradas (u. m.)",
            "Store_Type": "Establecimiento"
        },
        hover_data=[
            "Product_Id",
            "Product_Type"
        ]
    )

    fig.update_traces(marker=dict(size=5))

    if len(df) > 1 and df[COL_PRECIO].nunique() > 1:
        pendiente, intercepto = np.polyfit(
            df[COL_PRECIO],
            df[COL_VENTAS],
            1
        )

        x = np.linspace(
            df[COL_PRECIO].min(),
            df[COL_PRECIO].max(),
            100
        )

        fig.add_trace(
            go.Scatter(
                x=x,
                y=pendiente * x + intercepto,
                mode="lines",
                name="Tendencia lineal",
                line=dict(
                    color="#F8FAFC",
                    width=3,
                    dash="dash"
                )
            )
        )

    return aplicar_estilo(fig, 550)


def grafico_mapa_calor(cruce):
    fig = px.imshow(
        cruce,
        text_auto=".1f",
        aspect="auto",
        zmin=0,
        zmax=100,
        color_continuous_scale=[
            "#1E293B",
            "#0D9488",
            "#5EEAD4"
        ],
        labels={
            "x": "Rango de ventas",
            "y": "Rango de precios",
            "color": "Porcentaje (%)"
        },
        title="Distribución de ventas por segmento de precios"
    )

    return aplicar_estilo(fig, 450)