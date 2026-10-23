from hf_dataset_loader import HFDatasetLoader

# Cargamos el dataset Iris desde Hugging Face
loader = HFDatasetLoader("scikit-learn/iris", split="train")
df = loader.cargar_datos()

print("Primeras filas del dataset:")
print(df.head())

print("\nDimensiones del DataFrame:")
print(df.shape)

print("\nTipos de datos:")
print(df.dtypes)
