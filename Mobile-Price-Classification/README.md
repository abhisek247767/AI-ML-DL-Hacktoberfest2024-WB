# Mobile Price Classification

## Project Overview

Mobile Price Classification is a machine learning project that aims to predict the price range of mobile phones based on their features. The project utilizes three different machine learning algorithms: Decision Tree (DT), Random Forest (RF), and Support Vector Classification (SVC). The primary evaluation metrics include precision, recall, F1-score, accuracy, training score, and test score.

## Models Explored

The project employs the following machine learning models for classification:

1. **Decision Tree (DT)**: Decision trees are known for their simplicity and interpretability. This model creates a tree-like structure to classify mobile phones into price ranges based on their features.

2. **Random Forest (RF)**: Random Forest is an ensemble learning method that leverages multiple decision trees. It's well-suited for classification tasks and can improve prediction accuracy.

3. **Support Vector Classification (SVC)**: Support Vector Classification is a powerful classification algorithm. It works by finding the optimal hyperplane to separate different mobile phone price ranges.

## Model Evaluation

The project evaluates these models using various classification metrics:

- **Precision**: Measures the ratio of true positive predictions to all positive predictions, indicating the accuracy of positive predictions.

- **Recall**: Measures the ratio of true positive predictions to all actual positives, indicating the model's ability to identify all relevant instances.

- **F1-score**: Harmonic mean of precision and recall, providing a balanced measure of a model's accuracy.

- **Accuracy**: The proportion of correctly classified instances among all instances.

- **Training Score**: Reflects the model's performance on the training dataset.

- **Test Score**: Reflects the model's performance on the test dataset.

## Results

### Decision Tree (DT):

- Precision: 0.825125
- Recall: 0.825181
- F1-score: 0.824565
- Accuracy: 0.827500
- Training Score: 1.000000
- Test Score: 0.827500

### Random Forest (RF):

- Precision: 0.853572
- Recall: 0.855520
- F1-score: 0.854394
- Accuracy: 0.857500
- Training Score: 1.000000
- Test Score: 0.857500

### Support Vector Classification (SVC):

- Precision: 0.955357
- Recall: 0.954335
- F1-score: 0.954309
- Accuracy: 0.955000
- Training Score: 0.954375
- Test Score: 0.955000

The results demonstrate that the Support Vector Classification (SVC) model outperforms the others, achieving the highest precision, recall, F1-score, and accuracy. It shows great potential for accurately classifying mobile phone prices based on their features.

## Conclusion

Mobile Price Classification is a machine learning project that successfully predicts mobile phone price ranges. The project has explored three different models, with the Support Vector Classification (SVC) model emerging as the top performer. These results have practical applications in mobile pricing strategies and recommendations for both consumers and retailers.