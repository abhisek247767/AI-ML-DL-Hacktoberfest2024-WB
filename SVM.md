
# Support Vector Machine (SVM)

* Overview
Support Vector Machine (SVM) is a supervised learning algorithm used for both classification and regression tasks. It works by finding the optimal hyperplane that best separates different classes in a dataset. The main objective of SVM is to maximize the margin between the closest points of each class, known as support vectors.

SVM is particularly effective in high-dimensional spaces and can handle cases where the data is not linearly separable through the use of kernel functions, which transform data into higher dimensions for better separation.


![SVM_margin](https://github.com/user-attachments/assets/6062d26f-6406-4ea5-b79e-2463ead0ba75)




# How It Works

For linearly separable data, SVM finds the hyperplane that separates classes with the maximum margin. In cases where data is not linearly separable, SVM uses a kernel trick to project the data into a higher-dimensional space, making it easier to classify.

* Mathematical Representation
The decision boundary in SVM is defined as:


f(x)=w ^
T
 x+b


where:
* w: weight vector
* x: feature vector
* b: bias term

# Real-Life Applications

1. Spam Detection: SVM is used to classify emails as spam or not spam based on the text content and other features.

2. Disease Diagnosis: SVM helps in medical image classification, such as detecting whether a tumor is benign or malignant from MRI scans.

3. Customer Churn Prediction: Companies use SVM to predict whether a customer will churn based on their behavior, transaction history, and interaction patterns.

* SVM's ability to handle complex datasets, along with the flexibility of kernel functions, makes it suitable for a wide range of industries, from healthcare to finance.

