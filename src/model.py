from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

def create_mlp_model():
    return MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, solver='adam', random_state=42)

def train_model(X_train, y_train):
    mlp = create_mlp_model()
    mlp.fit(X_train, y_train)
    return mlp

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Accuracy Score:", accuracy_score(y_test, y_pred))

def perform_hyperparameter_tuning(X_train, y_train):
    param_grid = {
        'hidden_layer_sizes': [(50,50,50), (50,100,50), (100,)],
        'activation': ['tanh', 'relu'],
        'solver': ['sgd', 'adam'],
        'alpha': [0.0001, 0.05],
        'learning_rate': ['constant','adaptive'],
    }
    
    mlp = MLPClassifier(max_iter=1000, random_state=42)
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    grid_search = GridSearchCV(estimator=mlp, param_grid=param_grid, n_jobs=-1, cv=skf)
    
    grid_search.fit(X_train, y_train)
    
    print("Best parameters found: ", grid_search.best_params_)
    print("Best cross-validation score: {:.2f}".format(grid_search.best_score_))
    
    return grid_search.best_estimator_

def save_model(model, filename):
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")

def load_model(filename):
    return joblib.load(filename)