from src.data.load_data import load_data
from src.models.train_model import train_model
from src.models.predict_model import predict

if __name__ == '__main__':
    # Cargar datos
    data = load_data()

    # Entrenar el modelo
    model = train_model(data)

    # Realizar predicciones (con los mismos datos de prueba)
    X = data.drop('target', axis=1)
    predictions = predict(model, X)

    print(predictions)
