import pandas as pd

COL_VENTAS = "Product_Store_Sales_Total"
COL_PRECIO = "Product_MRP"

ORDEN_RANGOS = ["Bajo", "Medio", "Alto", "Muy alto"]


def calcular_indicadores(df):
    return {
        "ventas_totales": df[COL_VENTAS].sum(),
        "ventas_promedio": df[COL_VENTAS].mean(),
        "mediana": df[COL_VENTAS].median(),
        "productos": df["Product_Id"].nunique(),
        "establecimientos": df["Store_Id"].nunique(),
        "categorias": df["Product_Type"].nunique(),
        "observaciones": len(df)
    }


def calcular_metricas(df, columna):
    resumen = df.groupby(
        columna, observed=True
    ).agg(
        Ventas_totales=(COL_VENTAS, "sum"),
        Ventas_promedio=(COL_VENTAS, "mean"),
        Observaciones=(COL_VENTAS, "count")
    ).reset_index()

    total = resumen["Ventas_totales"].sum()

    resumen["Participacion_pct"] = (
        resumen["Ventas_totales"] / total * 100
        if total > 0 else 0
    )

    return resumen.sort_values(
        "Ventas_totales", ascending=False
    ).reset_index(drop=True)


def calcular_correlaciones(df):
    return {
        "Pearson": df[COL_PRECIO].corr(df[COL_VENTAS]),
        "Spearman": df[COL_PRECIO].rank().corr(
            df[COL_VENTAS].rank()
        )
    }


def correlaciones_por_establecimiento(df):
    resultados = []

    for tienda, grupo in df.groupby("Store_Type"):
        correlaciones = calcular_correlaciones(grupo)

        resultados.append({
            "Establecimiento": tienda,
            "Observaciones": len(grupo),
            **correlaciones
        })

    return pd.DataFrame(resultados)


def calcular_cruce_segmentos(df):
    return pd.crosstab(
        df["Price_Range"],
        df["Sales_Range"],
        normalize="index"
    ).reindex(
        index=ORDEN_RANGOS,
        columns=ORDEN_RANGOS
    ).fillna(0) * 100


def filtrar_datos(df, filtros):
    resultado = df.copy()

    for columna, valores in filtros.items():
        resultado = resultado[
            resultado[columna].isin(valores)
        ]

    return resultado