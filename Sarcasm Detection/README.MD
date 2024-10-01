## SARCASM DETECTION MODEL USING MACHINE LEARNING(NLP)
## **Project Overview**

The project is focused on building a sarcasm detection system using Machine Learning and Natural Language Processing (NLP) techniques. It uses the **Sarcasm Headlines Dataset** to classify news headlines as sarcastic or non-sarcastic. The system leverages text processing techniques and machine learning algorithms to identify and predict sarcasm in headlines.

## **Tools**

1. **Programming Language**: Python
2. **Libraries**:
   - **JSON**: For handling and loading the dataset.
   - **scikit-learn**: Machine learning library for model building and evaluation.
   - **TensorFlow**: Used for deep learning operations (embedding and neural networks).
   - **NLTK (Natural Language Toolkit)**: For text preprocessing and feature extraction.
   - **Pandas & Numpy**: Data handling and numerical operations.
   - **Matplotlib & Seaborn**: For data visualization and plotting results.

## **Processes**

1. **Data Loading**:
   - The dataset used is a JSON file (`Sarcasm_Headlines_Dataset.json`), which contains news headlines and a label indicating whether a headline is sarcastic (`1`) or not (`0`).
   - Initial loading of the dataset using Python’s `json` library.

2. **Data Preprocessing**:
   - **Tokenization** and **Vocabulary Building**: Creating word sequences and defining a maximum length for each headline.
   - **Padding and Truncation**: Ensuring all sequences have the same length using padding.
   - **Splitting the Dataset**: The data is split into training and testing sets.

3. **Model Building**:
   - The model uses various classifiers, including **Random Forest** and **Deep Learning Models** (e.g., a neural network in TensorFlow).
   - The Random Forest Classifier is implemented using `sklearn` to build a baseline for sarcasm detection.

4. **Evaluation**:
   - Model performance is evaluated using accuracy metrics, confusion matrix, and F1-score.
   - Comparisons are made between different models to choose the most effective one.

## **Model Results (Random Forest Classifier)**

- **Accuracy**: The Random Forest Classifier achieved a decent accuracy on the test set.
- **Confusion Matrix**: Showcases how many sarcastic headlines were correctly identified and the number of false positives/negatives.
- **F1-Score**: The F1-score was used to measure the model’s precision and recall balance, demonstrating its efficiency in sarcasm detection.
