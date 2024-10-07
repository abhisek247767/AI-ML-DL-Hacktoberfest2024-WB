# naive_bayes.py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer

# Sample dataset (text classification)
data = {
    'text': [
        "Free money now", 
        "Important meeting today", 
        "Win a lottery now", 
        "Let's discuss project", 
        "Exclusive offer just for you", 
        "Complete your homework",
        "Get your free trial now",
        "Meeting rescheduled"
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0]  # 1 = spam, 0 = non-spam
}

# Load data into pandas DataFrame
df = pd.DataFrame(data)

# Split the data into features and target
X = df['text']
y = df['label']

# Convert text data into feature vectors
vectorizer = CountVectorizer()
X_transformed = vectorizer.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.3, random_state=42)

# Initialize the Naive Bayes classifier
model = MultinomialNB()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Example usage for new data
new_texts = ["Claim your free prize", "Meeting tomorrow"]
new_X = vectorizer.transform(new_texts)
predictions = model.predict(new_X)
print(f"Predictions for new data: {predictions}")
