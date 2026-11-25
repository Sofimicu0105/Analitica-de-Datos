from pathlib import Path

import pandas as pd
import streamlit as st


PROYECTO = Path(__file__).resolve().parent.parent
RUTA_DATOS = PROYECTO / "datos" / "datos_procesados.csv"


@st.cache_data
def cargar_datos():
    df = pd.read_csv(RUTA_DATOS)
    return df