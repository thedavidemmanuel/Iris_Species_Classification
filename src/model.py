from sklearn.neural_network import MLPClassifier
import joblib

def train_model(X_train, y_train):
    mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, solver='adam', random_state=42)
    mlp.fit(X_train, y_train)
    return mlp

def save_model(model, filename):
    joblib.dump(model, filename)

def load_model(filename):
    return joblib.load(filename)