from src.data.load_data import load_data
from src.models.train_model import train_model

def test_train_model():
    data = load_data()
    model = train_model(data)
    assert model is not None, "El modelo no fue entrenado correctamente"
