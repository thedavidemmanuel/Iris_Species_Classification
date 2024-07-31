import numpy as np

def make_prediction(model, preprocessor, label_encoder, input_data):
    input_transformed = preprocessor.transform([input_data])
    prediction = model.predict(input_transformed)
    prediction_label = label_encoder.inverse_transform(prediction)
    return prediction_label[0]