# AdaBoost Algorithm

## Overview
**AdaBoost (Adaptive Boosting)** is an ensemble learning technique that combines multiple weak classifiers to create a strong classifier. It adjusts the weights of incorrectly classified instances so that subsequent classifiers focus more on difficult cases. It was introduced by Yoav Freund and Robert Schapire in 1996.

Unlike Random Forests that use bagging, AdaBoost uses **boosting**, meaning it trains models sequentially—each correcting the errors of the previous one.

---

## How It Works
1. Initialize equal weights for all training samples.
2. Train a weak classifier (like a decision stump).
3. Evaluate errors and increase weights of misclassified samples.
4. Repeat for a number of iterations.
5. Combine all weak learners into a final strong model.

Mathematically, the final classifier is a weighted sum of all weak learners.

---

## Real-Life Application
- **Fraud Detection:** Identifies subtle patterns of fraudulent activity.
- **Spam Filtering:** Boosts text-based classification accuracy.
- **Medical Diagnosis:** Improves detection accuracy on imbalanced datasets.
- **Face Detection:** AdaBoost was famously used in the Viola-Jones algorithm for real-time face detection.

---

## Implementation Example (Python)
Below is a concise AdaBoost example using `sklearn` on a simple classification dataset.

```python
from sklearn.datasets import make_classification
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Generate synthetic data
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, random_state=42)

# Step 2: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Create AdaBoost model
model = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=2),
    n_estimators=50,
    learning_rate=1.0,
    random_state=42
)

# Step 4: Train model
model.fit(X_train, y_train)

# Step 5: Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# output
# Model Accuracy: ~0.93