# Neural Networks

## What is a Neural Network?
* A Neural Network is a Machine Learning Program, which is used to make decisions and acts like a human brain.
* It is a collection of connected nodes called neurons.It is similar to neurons in our brain, which learn from different senses of our body.
* Neural networks are used to solve complex problems, which are not possible to solve by traditional programming.

## Types of Neural Networks:
1. Feedforward Neural Networks (FNNs):  In FNNs, the data flows only in one direction, from input layer to output layer.MLPs (Multilayer Perceptrons) are a specific type of feedforward neural network.

2. Recurrent Neural Networks (RNNs): In RNNs, the data flows in both directions, from input layer to output layer and from output layer to input layer. Examples include LSTM (Long Short Term Memory) and GRU (Gated Rectified Unit) 

3. Convolutional Neural Networks (CNNs):  Mostly used for image processing and computer vision tasks. They consist of convolutional layers that apply filters to input data, pooling layers that reduce dimensionality, and fully connected layers for classification. There are many nets which not limit to ImageNet, ResNet, etc....

4. Generative Adversial Networks (GAN's) : These Type of Neural Nets are mostly based on Generator-Discriminator Logic, where generator tries to create data and discriminator checks the authenticity of the output from generator. Used in Image,Audio and Video Generation

5. Autoencoders: Used for Unsupervised Learning tasks,such as dimensionality reduction and feature learning. Used to imprive qulaity of some image data.

6. Transformers : Primarily used in natural language processing (NLP) tasks. Transformers use self-attention mechanisms to process sequences of data in parallel, enabling efficient handling of long-range dependencies.

* Since this is an introductory article, we'll proceed with a Basic Feed Foward Network.
## How do they work?
* Nodes can be considered as a linear regression problem, where we have to give it an input data ,weights and bias to produce an output.

The mathematical representation of a linear function can be expressed as follows:
                  
                  $\sum w_i*x_i + \text{bias} = w_1*x_1 + w_2*x_2 + w_3*x3+\text{bias}$

## Steps of Feed Forward Neural Network

* Weight Assignment and Activation: Weights determine the importance of inputs, and an activation function decides whether a node "fires" based on whether the result exceeds a threshold, defining feedforward networks.

* Perceptrons vs. Sigmoid Neurons: Simple perceptrons use binary outputs, while more advanced neural networks use sigmoid neurons, which produce outputs between 0 and 1, making them more suitable for complex decision-making.

* Training with Supervised Learning: Neural networks are trained using labeled data and evaluated using cost functions, like Mean Squared Error (MSE). The goal is to minimize the cost function by adjusting weights and bias through gradient descent.

* Backpropagation: Backpropagation allows errors to propagate backward through the network, helping adjust weights to improve accuracy. This enables fine-tuning of the model during the training process.
