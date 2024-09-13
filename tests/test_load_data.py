from src.data.load_data import load_data

def test_load_data():
    data = load_data()
    assert data is not None, "La carga de datos falló"
    assert not data.empty, "El dataset está vacío"
    assert 'target' in data.columns, "La columna target no está presente en los datos"
