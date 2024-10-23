# Importing required libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# Generate some example data (sine wave sequence prediction)
def generate_sine_data(seq_length, num_samples):
    X, y = [], []
    for _ in range(num_samples):
        start = np.random.rand()
        x_seq = np.sin(np.linspace(start, start + 2 * np.pi, seq_length))
        X.append(x_seq)
        y.append(np.sin(start + 2 * np.pi))  # Next value in sequence
    return np.array(X), np.array(y)

# Hyperparameters
sequence_length = 50
num_samples = 1000
batch_size = 32
epochs = 50

# Generate and scale the data
X, y = generate_sine_data(sequence_length, num_samples)
scaler = MinMaxScaler(feature_range=(0, 1))
X_scaled = scaler.fit_transform(X)
X_scaled = np.reshape(X_scaled, (X_scaled.shape[0], X_scaled.shape[1], 1))  # Reshape for LSTM

# Building the LSTM model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(sequence_length, 1)))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X_scaled, y, epochs=epochs, batch_size=batch_size)

# Example prediction
test_input = np.sin(np.linspace(0, 2 * np.pi, sequence_length))
test_input_scaled = scaler.transform(test_input.reshape(1, -1))
test_input_scaled = np.reshape(test_input_scaled, (test_input_scaled.shape[0], test_input_scaled.shape[1], 1))
predicted_value = model.predict(test_input_scaled)
print(f"Predicted next value: {predicted_value[0][0]}")
