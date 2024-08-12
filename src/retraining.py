import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

def retrain_model(new_data_path, existing_data_path, model_path, pipeline_path):
    # Load the existing model and preprocessing pipeline
    model = joblib.load(model_path)
    pipeline = joblib.load(pipeline_path)

    # Load the existing and new data
    existing_data = pd.read_csv(existing_data_path)
    new_data = pd.read_csv(new_data_path)

    # Combine existing and new data
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)

    # Prepare the data
    X = combined_data.drop(columns=['Id', 'Species'])
    y = combined_data['Species']

    # Encode the target variable
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Preprocess the data
    X_train_processed = pipeline.fit_transform(X_train)
    X_test_processed = pipeline.transform(X_test)

    # Retrain the model
    model.fit(X_train_processed, y_train)

    # Make predictions
    y_pred = model.predict(X_test_processed)

    # Evaluate the retrained model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Retrained Model Accuracy: {accuracy:.3f}")
    print("Classification Report:\n", report)

    # Save the retrained model and updated pipeline
    joblib.dump(model, model_path)
    joblib.dump(pipeline, pipeline_path)
    print(f"Retrained model saved to {model_path}")
    print(f"Updated preprocessing pipeline saved to {pipeline_path}")

# Scenario for retraining:
# --------------------------------------------------
# This function is designed to be used when there is new Iris data that to incorporate
# into the existing model. Here are some scenarios to use this:
#
# 1. Regular Updates: If you collect new Iris measurements periodically, you can use this
#    function to update your model with the latest data, potentially improving its accuracy.
#
# 2. Seasonal Variations: If Iris characteristics change slightly with seasons, you could
#    retrain the model annually with the most recent year's data.
#
# 3. New Subspecies: If a new Iris subspecies is discovered, you could add this data to 
#    your model to help it recognize the new category.
#
# 4. Correction of Misclassifications: If you find that certain Irises were misclassified
#    in your original dataset, you can correct these in a new dataset and use this function
#    to update your model with the corrected data.
#
# 5. Expanding Dataset: As you collect more Iris samples over time, you can continually
#    expand your dataset and refine your model's performance.
#
# Remember: Before retraining, ensure that your new data follows the same format as the
# original dataset, with the same column names and structure.

# Example usage with relevant paths:
new_data_path = 'data/new_iris_data.csv'  # Path to your new data
existing_data_path = 'data/Iris.csv'  # Path to your original dataset
model_path = 'models/best_mlp_model.pkl'  # Path to your saved model
pipeline_path = 'models/preprocessing_pipeline.pkl'  # Path to your preprocessing pipeline

# To retrain the model, uncomment the following line:
# retrain_model(new_data_path, existing_data_path, model_path, pipeline_path)

# Note: Only run this when you actually have new data to add to your model.
# Running it without new data will essentially just retrain on the existing data, which may not be necessary.