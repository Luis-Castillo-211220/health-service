import pandas as pd
import joblib
import os

# Cargar el mejor modelo y el scaler
# path_model = './best_xgb_model2.pkl'
# path_scaler = '.\scaler.'

MODEL_PATH = os.path.join(os.path.dirname(__file__), './best_xgb_model2.pkl')
SCALER_PATH = os.path.join(os.path.dirname(__file__), './scaler.pkl')

best_xgb_model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def predecir_salud(edad: int, peso: float, consumo_agua: int, consumo_alimento: int, comportamiento: int, salud_general: float) -> float:
    datos = pd.DataFrame({
        "edad": [edad],
        "peso": [peso],
        "consumo_agua": [consumo_agua],
        "consumo_alimento": [consumo_alimento],
        "comportamiento": [comportamiento],
        "salud_general_%": [salud_general],
    })
    datos_escalados = scaler.transform(datos)
    prediccion = best_xgb_model.predict(datos_escalados)
    return prediccion[0]
