import numpy as np
from sklearn.metrics import accuracy_score,r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, Perceptron
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

x, y = make_classification(n_samples=100, n_features=2, n_redundant=0, n_informative=1,n_classes=2, random_state=41, n_clusters_per_class=1,hypercube=False, class_sep=10)

# method 1
def perceptron(x,y):
    x = np.insert(x, 0, 1, axis=1)
    weights = np.ones(x.shape[1])
    lr = 0.5
    epochs = 2000
    for _ in range(epochs):
        j = np.random.randint(x.shape[0])
        y_pred = step(np.dot(x[j], weights))
        weights = weights + lr * (y[j] - y_pred) * x[j]

    return weights[0], weights[1:]

def step(z):
    return 1 if z > 0 else 0

intercept, coefficients = perceptron(x,y)

print("intercepts: ", intercept, "coefficients: ", coefficients)

m = - (coefficients[0] / coefficients[1])
b = - (intercept / coefficients[1])

print("slope: ", m, "intercept: ", b)

x_input = np.linspace(-3,3,10)
y_input = m * x_input + b

# method 2
def sigmoid_method(x,y):
    x = np.insert(x, 0, 1, axis=1)
    weights = np.ones(x.shape[1])
    lr = 0.5
    epochs = 2000
    for _ in range(epochs):
        j = np.random.randint(x.shape[0])
        y_pred = sigmoid(np.dot(x[j], weights))
        weights = weights + lr * (y[j] - y_pred) * x[j]

    return weights[0], weights[1:]

def sigmoid(z):
    return 1 / (1+np.exp(-z))

intercept_2, coefficients_2 = sigmoid_method(x,y)

print("intercepts: ", intercept_2, "coefficients: ", coefficients_2)

m_2 = - (coefficients_2[0] / coefficients_2[1])
b_2 = - (intercept_2 / coefficients_2[1])

print("slope: ", m_2, "intercept: ", b_2)

x_input_2 = np.linspace(-3,3,10)
y_input_2 = m_2 * x_input_2 + b_2

# method 3
model = LogisticRegression(penalty=None, solver='sag').fit(x,y)
print(model.coef_)
m_3 = -(model.coef_[0][0] / model.coef_[0][1])
b_3 = -(model.intercept_ / model.coef_[0][1])

print("slope: ", m_3, "intercept: ", b_3)

x_input_3 = np.linspace(-3,3,10)
y_input_3 = m_3 * x_input_3 + b_3

# method 4
def gdr_method(x,y):
    x = np.insert(x, 0, 1, axis=1)
    weights = np.ones(x.shape[1])
    lr = 0.5
    epochs = 5000
    for _ in range(epochs):
        y_pred = sigmoid2(np.dot(x, weights))
        weights = weights + lr * (np.dot((y - y_pred), x) / x.shape[0])

    return weights[0], weights[1:]

def sigmoid2(z):
    return 1 / (1+np.exp(-z))

intercept_3, coefficients_3 = gdr_method(x,y)

print("intercepts: ", intercept_3, "coefficients: ", coefficients_3)

m_4 = - coefficients_3[0] / coefficients_3[1]
b_4 = - intercept_3 / coefficients_3[1]

print("slope: ", m_4, "intercept: ", b_4)

x_input_4 = np.linspace(-3,3,10)
y_input_4 = m_4 * x_input_4 + b_4

plt.figure(figsize=(10,6))
plt.scatter(x[:,0],x[:,1],c=y,cmap='winter',edgecolors='b')
# plt.plot(x_input,y_input,c='red')
# plt.plot(x_input_2,y_input_2,c='black')
plt.plot(x_input_3,y_input_3,c='yellow')
plt.plot(x_input_4,y_input_4,c='red')
plt.show()
