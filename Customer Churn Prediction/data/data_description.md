# Dataset Description

## Telco Customer Churn Dataset

This dataset contains information about telecom customers and whether they churned (left the company).

## Download Instructions

Download the dataset from Kaggle:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Save as: `data/churn_data.csv`

## Features

Total: 21 columns, 7043 rows

### Target Variable
- **Churn**: Whether customer left (Yes/No)

### Customer Information
- **customerID**: Unique identifier
- **gender**: Male/Female
- **SeniorCitizen**: 0 or 1
- **Partner**: Yes/No
- **Dependents**: Yes/No

### Account Information
- **tenure**: Months as customer
- **Contract**: Month-to-month, One year, Two year
- **PaperlessBilling**: Yes/No
- **PaymentMethod**: Electronic check, Mailed check, Bank transfer, Credit card
- **MonthlyCharges**: Monthly bill amount
- **TotalCharges**: Total amount charged

### Services
- **PhoneService**: Yes/No
- **MultipleLines**: Yes/No/No phone service
- **InternetService**: DSL/Fiber optic/No
- **OnlineSecurity**: Yes/No/No internet
- **OnlineBackup**: Yes/No/No internet
- **DeviceProtection**: Yes/No/No internet
- **TechSupport**: Yes/No/No internet
- **StreamingTV**: Yes/No/No internet
- **StreamingMovies**: Yes/No/No internet