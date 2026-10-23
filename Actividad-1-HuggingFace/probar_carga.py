from hf_dataset_loader import HFDatasetLoader
from dataset_summarizer import DatasetSummarizer

# Obtenemos los datos desde Hugging Face
loader = HFDatasetLoader("scikit-learn/iris", split="train")
df = loader.cargar_datos()

print("Primeras filas del dataset:")
print(df.head())

print("\nDimensiones del DataFrame:")
print(df.shape)

# Generamos un resumen de los datos cargados
resumidor = DatasetSummarizer(df, "Iris")
ruta_resumen = resumidor.guardar_resumen("resumen_prueba.txt")

print(f"\nResumen generado correctamente: {ruta_resumen}")
print("\nContenido del resumen:")
print(resumidor.generar_resumen())
