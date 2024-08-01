import joblib

def load_model(model_filename):
    return joblib.load(model_filename)

def load_preprocessing_pipeline(pipeline_filename):
    return joblib.load(pipeline_filename)

def predict(model, preprocessing_pipeline, input_data):
    processed_data = preprocessing_pipeline.transform(input_data)
    prediction = model.predict(processed_data)
    return prediction

def predict_proba(model, preprocessing_pipeline, input_data):
    processed_data = preprocessing_pipeline.transform(input_data)
    probabilities = model.predict_proba(processed_data)
    return probabilities