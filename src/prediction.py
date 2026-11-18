import joblib
from config.settings import MODEL_PATH

def predict_rice_packets(land_size=3.5):
    model = joblib.load(MODEL_PATH)

    prediction = model.predict([[land_size]])
    result = round(prediction[0])
    print("Predicted Rice Packets:", result)
    return result
