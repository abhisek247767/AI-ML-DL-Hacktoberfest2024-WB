import numpy as np


def predict(x, m, b):
    return m * x + b


def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def linear_regression(X, Y, learning_rate=0.01, epochs=10000):
    m = 0
    b = 0

    n = len(X)

    for _ in range(epochs):
        y_pred = predict(X, m, b)

        m_gradient = -(2 / n) * np.sum(X * (Y - y_pred))
        b_gradient = -(2 / n) * np.sum(Y - y_pred)

        m -= learning_rate * m_gradient
        b -= learning_rate * b_gradient

    return m, b

def main():
    X = np.array([1, 2, 3, 4, 6])
    Y = np.array([1, 2, 3, 3.5, 5])

    learning_rate = 0.01
    epochs = 1000
    m, b = linear_regression(X, Y, learning_rate, epochs)

    predictions = predict(X, m, b)

    print(f"Slope (m): {m}")
    print(f"Intercept (b): {b}")
    print(f"Predictions: {predictions}")
    print(f"Mean Squared Error: {mean_squared_error(Y, predictions)}")


if __name__ == "__main__":
    main()
