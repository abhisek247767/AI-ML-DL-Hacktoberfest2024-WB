# Import necessary libraries
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

# Generate synthetic binary classification dataset with two features
x, y = make_classification(n_samples=100, n_features=2, n_redundant=0, n_informative=1, 
                           n_classes=2, random_state=41, n_clusters_per_class=1, 
                           hypercube=False, class_sep=10)

# Method 1: Perceptron using a step function
def perceptron(x, y):
    # Add bias term to the input data
    x = np.insert(x, 0, 1, axis=1)
    weights = np.ones(x.shape[1])  # Initialize weights
    lr = 0.5                       # Learning rate
    epochs = 2000                  # Number of iterations

    # Training using stochastic gradient descent
    for _ in range(epochs):
        j = np.random.randint(x.shape[0])
        y_pred = step(np.dot(x[j], weights))
        weights += lr * (y[j] - y_pred) * x[j]  # Update weights based on prediction error

    return weights[0], weights[1:]  # Return intercept and coefficients

# Step function for perceptron method
def step(z):
    return 1 if z > 0 else 0

# Get intercept and coefficients for perceptron method
intercept, coefficients = perceptron(x, y)
m = -coefficients[0] / coefficients[1]
b = -intercept / coefficients[1]

# Generate decision boundary for perceptron
x_input = np.linspace(-3, 3, 10)
y_input = m * x_input + b

# Method 2: Sigmoid activation with stochastic gradient descent
def sigmoid_method(x, y):
    x = np.insert(x, 0, 1, axis=1)
    weights = np.ones(x.shape[1])
    lr = 0.5
    epochs = 2000

    for _ in range(epochs):
        j = np.random.randint(x.shape[0])
        y_pred = sigmoid(np.dot(x[j], weights))
        weights += lr * (y[j] - y_pred) * x[j]

    return weights[0], weights[1:]

# Sigmoid function for logistic regression-like model
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Get intercept and coefficients for sigmoid method
intercept_2, coefficients_2 = sigmoid_method(x, y)
m_2 = -coefficients_2[0] / coefficients_2[1]
b_2 = -intercept_2 / coefficients_2[1]

# Generate decision boundary for sigmoid method
x_input_2 = np.linspace(-3, 3, 10)
y_input_2 = m_2 * x_input_2 + b_2

# Method 3: Logistic Regression from sklearn
model = LogisticRegression(penalty=None, solver='sag').fit(x, y)
m_3 = -model.coef_[0][0] / model.coef_[0][1]
b_3 = -model.intercept_ / model.coef_[0][1]

# Generate decision boundary for logistic regression model
x_input_3 = np.linspace(-3, 3, 10)
y_input_3 = m_3 * x_input_3 + b_3

# Method 4: Gradient Descent with sigmoid function
def gdr_method(x, y):
    x = np.insert(x, 0, 1, axis=1)
    weights = np.ones(x.shape[1])
    lr = 0.5
    epochs = 5000

    for _ in range(epochs):
        y_pred = sigmoid(np.dot(x, weights))
        weights += lr * (np.dot((y - y_pred), x) / x.shape[0])

    return weights[0], weights[1:]

# Sigmoid function for gradient descent
def sigmoid2(z):
    return 1 / (1 + np.exp(-z))

# Get intercept and coefficients for gradient descent method
intercept_3, coefficients_3 = gdr_method(x, y)
m_4 = -coefficients_3[0] / coefficients_3[1]
b_4 = -intercept_3 / coefficients_3[1]

# Generate decision boundary for gradient descent method
x_input_4 = np.linspace(-3, 3, 10)
y_input_4 = m_4 * x_input_4 + b_4

# Plotting results
plt.figure(figsize=(10, 6))
plt.scatter(x[:, 0], x[:, 1], c=y, cmap='winter', edgecolors='b', label="Data Points")
plt.plot(x_input, y_input, c='red', label="Perceptron")
plt.plot(x_input_2, y_input_2, c='black', label="Sigmoid Method")
plt.plot(x_input_3, y_input_3, c='yellow', label="Logistic Regression")
plt.plot(x_input_4, y_input_4, c='green', label="Gradient Descent with Sigmoid")

# Adding labels and legend
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.title("Decision Boundaries for Different Classification Methods")
plt.show()
