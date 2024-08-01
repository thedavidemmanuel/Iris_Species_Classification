from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.metrics import accuracy_score
import uvicorn

app = FastAPI()

# Updated file paths
MODEL_PATH = "models/best_mlp_model.pkl"
PIPELINE_PATH = "models/preprocessing_pipeline.pkl"

# Load the model and preprocessing pipeline
model = joblib.load(MODEL_PATH)
preprocessing_pipeline = joblib.load(PIPELINE_PATH)

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class TrainingData(BaseModel):
    features: list
    labels: list

@app.post("/predict")
async def predict(iris: IrisFeatures):
    try:
        # Convert input to DataFrame
        features_df = pd.DataFrame([iris.dict()])
        
        # Rename columns to match what the pipeline expects
        features_df.columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
        
        # Apply preprocessing
        processed_features = preprocessing_pipeline.transform(features_df)
        
        # Make prediction
        prediction = model.predict(processed_features)
        
        # Get the class label
        class_labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
        class_label = class_labels[prediction[0]]
        
        return {"prediction": int(prediction[0]), "class_label": class_label}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/retrain")
async def retrain(data: TrainingData, background_tasks: BackgroundTasks):
    background_tasks.add_task(retrain_model, data)
    return {"message": "Retraining started in the background"}

@app.get("/model-info")
async def model_info():
    return {
        "model_type": type(model).__name__,
        "input_features": 4,
        "output_classes": 3,
        "hidden_layer_sizes": model.hidden_layer_sizes
    }

def retrain_model(data: TrainingData):
    try:
        X = pd.DataFrame(data.features, columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])
        y = pd.Series(data.labels)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        new_preprocessing_pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('selector', SelectKBest(score_func=f_classif, k='all'))
        ])
        
        X_train_processed = new_preprocessing_pipeline.fit_transform(X_train, y_train)
        X_test_processed = new_preprocessing_pipeline.transform(X_test)
        
        new_model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1000, random_state=42)
        new_model.fit(X_train_processed, y_train)
        
        accuracy = accuracy_score(y_test, new_model.predict(X_test_processed))
        
        if accuracy > 0.9:  # You can adjust this threshold
            joblib.dump(new_model, MODEL_PATH)
            joblib.dump(new_preprocessing_pipeline, PIPELINE_PATH)
            global model, preprocessing_pipeline
            model = new_model
            preprocessing_pipeline = new_preprocessing_pipeline
            print(f"Model retrained and saved with accuracy: {accuracy}")
        else:
            print(f"New model accuracy ({accuracy}) is not better than the threshold. Keeping the old model.")
    except Exception as e:
        print(f"Error during retraining: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)