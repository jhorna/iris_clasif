from sklearn.datasets import load_iris
import pandas as pd

def load_data():
    """Carga el dataset Iris de sklearn."""
    try:
        iris = load_iris()
        data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        data['target'] = iris.target
        return data
    except Exception as e:
        print(f"Error cargando los datos: {e}")
        return None
