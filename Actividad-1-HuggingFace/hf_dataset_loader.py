import pandas as pd
from datasets import load_dataset


class HFDatasetLoader:
    def __init__(self, dataset_id, split="train"):
        self.dataset_id = dataset_id
        self.split = split

    def cargar_datos(self):
        """Carga un dataset de Hugging Face y lo convierte a DataFrame."""
        try:
            dataset = load_dataset(self.dataset_id, split=self.split)
            dataframe = dataset.to_pandas()

            if not isinstance(dataframe, pd.DataFrame):
                raise TypeError("No se pudo obtener un DataFrame válido.")

            return dataframe

        except Exception as error:
            raise RuntimeError(
                f"No fue posible cargar el dataset '{self.dataset_id}' "
                f"con el split '{self.split}': {error}"
            ) from error
