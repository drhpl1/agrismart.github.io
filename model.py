import pickle

global model, scaler

def load():
    global model, scaler
    model = pickle.load(open('model/model_rf.pkl', 'rb'))
    scaler = pickle.load(open('model/scaler.pkl', 'rb'))

def prediksi(data):
    # Standardisasi data
    data = scaler.transform(data)

    # Prediksi hasil Status
    prediksi = int(model.predict(data))

    return  prediksi