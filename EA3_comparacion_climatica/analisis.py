from pathlib import Path
import pandas as pd

ruta_datos = Path(__file__).resolve().parent / "datos"

for ciudad, archivo in [
    ("Medellín", "medellin.csv"),
    ("Madrid", "madrid.csv")
]:
    datos = pd.read_csv(ruta_datos / archivo, skiprows=3)

    total_dias = len(datos)

    dias_lluviosos = (datos["precipitation_sum (mm)"] > 0).sum()
    dias_mayores_25 = (datos["temperature_2m_max (°C)"] > 25).sum()

    porcentaje_lluvia = dias_lluviosos / total_dias * 100
    porcentaje_temperatura = dias_mayores_25 / total_dias * 100

    print(f"\n{ciudad}")
    print(f"Días con precipitación: {porcentaje_lluvia:.2f}%")
    print(f"Días con temperatura máxima superior a 25 °C: {porcentaje_temperatura:.2f}%")