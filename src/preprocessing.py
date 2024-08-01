import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred while loading the data: {str(e)}")

def check_data_quality(data):
    missing_values = data.isnull().sum()
    print("Missing values in each column:\n", missing_values)
    
    duplicate_rows = data[data.duplicated()]
    print("\nNumber of duplicate rows:", len(duplicate_rows))

def preprocess_data(data, target_column='Species'):
    X = data.drop(columns=['Id', target_column])
    y = data[target_column]
    
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)
    
    numerical_features = X.columns.tolist()
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features)
        ])
    
    selector = SelectKBest(score_func=f_classif, k='all')
    
    preprocessing_pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('selector', selector)
    ])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    X_train_processed = preprocessing_pipeline.fit_transform(X_train, y_train)
    X_test_processed = preprocessing_pipeline.transform(X_test)
    
    return X_train_processed, X_test_processed, y_train, y_test, preprocessing_pipeline, label_encoder

def save_preprocessing_pipeline(pipeline, filename):
    joblib.dump(pipeline, filename)
    print(f"Preprocessing pipeline saved to {filename}")

def load_preprocessing_pipeline(filename):
    return joblib.load(filename)