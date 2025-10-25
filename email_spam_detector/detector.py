from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

data = fetch_openml('SMS Spam Collection', version=1, as_frame=True)
texts = data.data['text']
labels = data.target

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)
pred = model.predict(X_test)

print(accuracy_score(y_test, pred))
print(classification_report(y_test, pred))


#just basic ml code for printing the accuracy score and the report produced by the detector
