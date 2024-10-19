# Housing Price Prediction 

This project involves predicting house prices using machine learning algorithms. The workflow covers data preprocessing, handling missing values, feature engineering, outlier detection, and model building using algorithms like Linear Regression and Decision Tree.

## Steps Involved:

### 1. Data Collection and Loading:
We start by loading the housing dataset into a pandas DataFrame and perform an initial exploratory analysis.

### 2. Data Cleaning:
- Removed unnecessary columns (e.g., 'area_type', 'society', etc.)
- Handled missing values by removing rows with null data.
- Converted non-standard total square footage entries to numeric.

### 3. Feature Engineering:
- Created a new feature 'price_per_sqft' to standardize pricing.
- Dimensionality reduction: Locations with fewer than 10 data points were labeled 'other'.
- Added BHK (number of bedrooms) by parsing the 'size' column.

### 4. Outlier Removal:
- Used domain-specific knowledge (like minimum square footage per BHK) and statistical methods (mean, standard deviation) to remove outliers from the dataset.

### 5. Model Training:
- Split the dataset into training and testing sets.
- Trained a Linear Regression model and evaluated its performance using K-fold cross-validation.

### 6. Hyperparameter Tuning:
- Applied GridSearchCV to test multiple regression algorithms (Linear Regression, Lasso, Decision Tree) and their parameters.
- Linear Regression provided the best results.

### 7. Prediction:
The model can predict house prices based on location, square footage, number of bathrooms, and BHK.

### 8. Visualization:
Scatter plots and histograms were used to visualize the relationships between features, prices, and outliers.

## Technologies Used:
- Python, Pandas, NumPy, Matplotlib
- Machine Learning: Scikit-learn
- Algorithms: Linear Regression, Decision Tree

## Conclusion:
This project demonstrates how to build a predictive model for house prices by preprocessing data, removing outliers, and applying machine learning algorithms." > project_overview.md
