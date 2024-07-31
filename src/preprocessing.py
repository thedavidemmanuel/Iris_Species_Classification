import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    X = data.drop(columns=['Id', 'Species'])
    y = data['Species']

    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

    numerical_features = X.columns.tolist()
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features)
        ])
    
    X_transformed = preprocessor.fit_transform(X)
    return X_transformed, y, preprocessor, label_encoder