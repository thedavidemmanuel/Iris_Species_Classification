# Iris Species Classification

## Brief

This project aims to classify iris flowers into three species using sepal and petal measurements from the classic Iris dataset introduced by R.A. Fisher in 1936. The dataset contains 150 samples, with 50 samples for each of the three iris species.

## Project Description

This project utilizes a Multi-layer Perceptron (MLP) classifier to classify iris flowers into three species based on their sepal and petal measurements. The model architecture and hyperparameters were optimized using grid search with cross-validation to achieve the best performance.

## Workflow for Proposed Project

1. Data Preprocessing
2. Model Training
3. Model Evaluation
4. Prediction

## Project Structure

```

iris-species-classification/
│
├── data/
│ └── Iris.csv
│
├── notebooks/
│ └── iris_classification.ipynb
│
├── src/
│ ├── data_preprocessing.py
│ ├── model.py
│ └── evaluation.py
│
├── models/
│ └── iris_model.pkl
│
├── requirements.txt
│
└── README.md

```

## Setup Instructions

Ensure you have Python 3.7+ installed.

1. Clone this repository:
   ```sh
   git clone https://github.com/thedavidemmanuel/Iris_Species_Classification.git
   cd iris-species-classification
   ```

````

2. Create a virtual environment:

   ```sh
   python -m venv env
   ```

3. Activate the virtual environment:

   - On Windows: `env\Scripts\activate`
   - On Unix or MacOS: `source env/bin/activate`

4. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Data Description

The dataset contains 150 samples, with 50 samples for each of the three iris species. Each sample has four features:

1. Sepal Length (cm)
2. Sepal Width (cm)
3. Petal Length (cm)
4. Petal Width (cm)

The target variable is the iris species:

- Iris setosa
- Iris versicolor
- Iris virginica

## Preprocessing Steps

The `src/data_preprocessing.py` file contains the following main functions:

- `load_and_preprocess_data(file_path)`: Loads the CSV file, splits features and target, scales the features, and saves the scaler.
- `load_scaler()`: Loads the saved StandardScaler object.

To run preprocessing:

```sh
python src/data_preprocessing.py
```

## Model Training

The `src/model.py` file contains the following main functions:

- `create_model()`: Creates and compiles the MLP classifier.
- `train_model(X_train, y_train, epochs=100, batch_size=32)`: Trains the model with early stopping.
- `evaluate_model(model, X_test, y_test)`: Evaluates the trained model on test data.

To train the model:

```sh
python src/model.py
```

## Model Evaluation

The `src/evaluation.py` file contains the following main functions:

- `plot_training_history(history)`: Plots the training and validation accuracy/loss.
- `classification_report(y_true, y_pred)`: Generates a classification report.

To evaluate the model:

```sh
python src/evaluation.py
```

## Usage

1. Open and run the Jupyter notebook `notebooks/iris_classification.ipynb` for a step-by-step walkthrough of the project.
2. Alternatively, you can use the Python scripts in the `src/` directory for data preprocessing, model training, and evaluation.

## Model Files

- **Pickle (.pkl) file**:
  - Location: `models/iris_model.pkl`
  - Purpose: Stores the trained MLP model.

## Notebook

The Jupyter notebook `notebooks/iris_classification.ipynb` provides an interactive environment for data analysis, model training, and result visualization. To use the notebook:

1. Ensure you have Jupyter installed: `pip install jupyter`
2. Navigate to the project directory and start Jupyter:
   ```sh
   jupyter notebook
   ```
3. Open `notebooks/iris_classification.ipynb` from the Jupyter interface.

The notebook includes cells for:

- Data loading and exploration
- Preprocessing steps
- Model creation and training
- Evaluation and visualization of results

## Results

Our best model achieved an accuracy of X% on the test set. Detailed evaluation metrics and visualizations can be found in the notebook.

## Future Work

- Experiment with other classification algorithms
- Implement feature engineering techniques
- Deploy the model as a web application

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For any queries, please open an issue in this repository.

```

```
````
