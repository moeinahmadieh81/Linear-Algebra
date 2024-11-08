# Linear Regression with Training and Test Data

This Python project demonstrates the implementation of linear regression using `numpy.linalg.lstsq` for solving a system of linear equations. It uses a dataset, splits it into training and test sets, and fits a linear regression model to the training data. The model is then used to estimate values from the test data, and the results are visualized using `matplotlib`.

## Features

- **Data Preprocessing**: Reads and splits a dataset into training and test sets.
- **Linear Regression**: Uses least squares method to fit a line to the training data.
- **Model Evaluation**: Estimates values for test data and computes errors.
- **Data Visualization**: Plots the training data, test data, and the fitted regression line.

## Requirements

- **Python 3.x**
- **NumPy**
- **Pandas**
- **Matplotlib**

Install the required libraries using:
```bash
pip install numpy pandas matplotlib
```
## Running the Code
- Clone this repository or copy the code into a Python file (e.g., linear_regression.py).
- Ensure you have a dataset (e.g., data.csv) with two columns where the first column represents the independent variable and the second column represents the dependent variable.
- Open a terminal, navigate to the directory where the script is located, and run:
```bash
python main.py
```
