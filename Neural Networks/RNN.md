# Recurrent Neural Networks (RNNs)

## What is an RNN?
- **Recurrent Neural Networks (RNNs)** are a class of neural networks designed for sequential data, where the output from one step is used as input for the next.
- RNNs are commonly used in tasks involving time series, natural language processing (NLP), and speech recognition because they retain information from previous inputs through internal memory (hidden states).

## How do RNNs work?
- RNNs introduce the concept of loops in neural networks, which allows information to persist.
- The key difference from Feedforward Neural Networks is that RNNs have connections that form directed cycles, making them suitable for sequential data.
- The formula for the hidden state in an RNN can be expressed as:

$h_t = f(W_h h_{t-1} + W_x x_t + b)$

where:
- $h_t$ is the hidden state at time $t$,
- $W_h$ is the weight matrix for the hidden state,
- $W_x$ is the weight matrix for the input, and
- $x_t$ is the input at time $t$.

## Types of RNNs
1. **Vanilla RNNs**: Basic RNNs with simple loops that may struggle with long-term dependencies.
2. **Long Short-Term Memory (LSTM)**: A type of RNN designed to solve the vanishing gradient problem, capable of learning long-range dependencies by using gates to control the flow of information.
3. **Gated Recurrent Units (GRU)**: A simpler variant of LSTMs that also addresses the vanishing gradient problem but with fewer gates.

## Applications of RNNs
- **Time Series Forecasting**: Predicting future values in sequential data like stock prices or weather patterns.
- **Natural Language Processing (NLP)**: Used in tasks like language modeling, text generation, machine translation, and sentiment analysis.
- **Speech Recognition**: Processing sequential audio data to recognize speech patterns and convert them to text.
- **Video Analysis**: Understanding and predicting actions in video frames over time.

## Challenges with RNNs
- **Vanishing Gradient Problem**: During training, gradients used in backpropagation through time (BPTT) can diminish, making it difficult for the network to learn long-term dependencies.
- **Exploding Gradients**: The opposite problem where gradients grow excessively large, making training unstable.

## Advanced Variants
- **Bi-directional RNNs**: Process data in both forward and backward directions, improving performance in tasks like speech and language processing.
- **Deep RNNs**: Stacking multiple layers of RNNs to model more complex patterns in sequential data.

