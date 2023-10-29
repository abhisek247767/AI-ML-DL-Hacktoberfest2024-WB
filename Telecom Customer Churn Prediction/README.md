# Telecom Customers Churn Prediction

![Telecom Customers Churn Prediction](https://github.com/MB-Shihab-Aaqil-Ahamed/Machine-Learning-Projects/blob/master/Telecom%20Customers%20Churn%20Prediction/Images/Customer_churn.jpg)


## Project Overview
In this hands-on project, we will train several classification algorithms, namely Logistic Regression, Support Vector Machine, K-Nearest Neighbors, and Random Forest Classifier, to predict the churn rate of Telecommunication Customers.

Telecom service providers use customer attrition analysis as a key business metric because retaining an existing customer is more cost-effective than acquiring a new one. Machine Learning algorithms help analyze customer attrition rates based on factors such as services subscribed, tenure rate, gender, senior citizen status, payment method, etc.

Among all the trained models, the Random Forest Classifier algorithm produced the highest Area under the ROC curve (AUC).

## Tools
This project utilizes the following tools and libraries:

- Anaconda: Package manager and environment manager for Python.
- Python: Programming language used for developing the AI model.
- Scikit-Learn: Machine learning library for Python.
- Matplotlib: Data visualization library in Python.
- Seaborn: Data visualization library based on Matplotlib.

## Tasks
This project on Telecom Customers Churn Prediction is divided into the following tasks:

1. Understand the problem statement and business case.
2. Import libraries/datasets and perform Exploratory Data Analysis.
3. Perform Data Visualization.
4. Prepare the data before model training.
5. Train and Evaluate a Logistic Regression model.
6. Train and Evaluate a Support Vector Machine Model.
7. Train and Evaluate a Random Forest Classifier model.
8. Train and Evaluate a K-Nearest Neighbor model.
9. Train and Evaluate a Naive Bayes Classifier model.
10. Compare the trained models by calculating AUC score and plot ROC curve.

## Model Results (Random Forest Classifier)
- Accuracy: ~96% label accuracy
- Precision: ~96% labeled as Retained customers and ~94% labeled as churned customers
- Recall: ~99% labeled as Retained customers and ~76% labeled as churned customers

Please note that the model's performance can potentially be further improved using the "Grid Search" method. For more information on Grid Search, check out this resource: [Hyperparameter Optimization with Random Search and Grid Search](https://machinelearningmastery.com/hyperparameter-optimization-with-random-search-and-grid-search/).
