# Iris Species Classification

## Overview

Classify iris flowers into three species using sepal and petal measurements from the classic Iris dataset introduced by R.A. Fisher in 1936.

## Dataset

The dataset contains 150 samples, with 50 samples for each of the three iris species. Each sample has four features:

1. Sepal Length (cm)
2. Sepal Width (cm)
3. Petal Length (cm)
4. Petal Width (cm)

The target variable is the iris species:

- Iris setosa
- Iris versicolor
- Iris virginica

## Project Overview

This project aims to classify iris flowers into three species based on their sepal and petal measurements. We use the classic Iris dataset, which was introduced by R.A. Fisher in his 1936 paper "The Use of Multiple Measurements in Taxonomic Problems".

## Dataset Description

The dataset contains 150 samples, with 50 samples for each of the three iris species. Each sample has four features:

1. Sepal Length (cm)
2. Sepal Width (cm)
3. Petal Length (cm)
4. Petal Width (cm)

The target variable is the iris species, which can be one of:

- Iris setosa
- Iris versicolor
- Iris virginica

## Project Structure

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
├── requirements.txt
│
└── README.md

## Setup

To set up the project environment:

1. Clone this repository
2. Navigate to the project directory
3. Create a virtual environment:

   ```sh
   python -m venv env
   ```

4. Activate the virtual environment:

   - On Windows: `env\Scripts\activate`
   - On Unix or MacOS: `source env/bin/activate`

5. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

   Note: Make sure you have Python installed on your system before proceeding with the above steps.

## Usage

1. Open and run the Jupyter notebook `notebooks/iris_classification.ipynb` for a step-by-step walkthrough of the project.
2. Alternatively, you can use the Python scripts in the `src/` directory for data preprocessing, model training, and evaluation.

## Model

We use a Multi-layer Perceptron (MLP) classifier for this task. The model architecture and hyperparameters were optimized using grid search with cross-validation.

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
