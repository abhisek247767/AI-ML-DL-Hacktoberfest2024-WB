from flask import Flask, request, jsonify, render_template
import json
import pickle
import pandas as pd
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__, static_url_path='/static')

# Load the saved model and related data
with open('model.pkl', 'rb') as f:
    knn_model = pickle.load(f)
    cv = pickle.load(f)
    new_cv = pickle.load(f)
    df_idf = pickle.load(f)
    data = pickle.load(f)
    all_symptoms = pickle.load(f)
    input_symptoms = pickle.load(f)
    input_age = pickle.load(f)
    input_gender = pickle.load(f)
    top_diseases = pickle.load(f)
    indices = pickle.load(f)
    distances = pickle.load(f)
    k = pickle.load(f)
    cols = pickle.load(f)
    df = pickle.load(f)
    docs = pickle.load(f)
    word_count_vector = pickle.load(f)
    tfidf_transformer = pickle.load(f)
    new_word_count_vector = pickle.load(f)
    new_tfidf_transformer = pickle.load(f)
    input_vector = pickle.load(f)

@app.route('/')
def index():
    return render_template('new.html')

@app.route('/old')
def innew():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    # Load data from JSON file
    req_data = request.json
    print(req_data)
    disease = req_data['disease']
    age = req_data['age']
    gender = req_data['gender']
    with open('./static/wholeData.json') as file:
        data = json.load(file)
    
    data = [d for d in data if d['name'] == disease and d['ageGroup'] == age and d['gender'] == gender]
    
    return jsonify(data[0])

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    req_data = request.json
    input_age = req_data['age']
    input_gender = req_data['gender']
    input_symptoms = req_data['symptoms']
    rejected_symptoms = req_data['rejected_symptoms']

    if(len(input_symptoms) < 3):
        k = 5
    elif(len(input_symptoms) < 5):
        k = 3
    elif(len(input_symptoms) < 7):
        k = 2
    else:
        k = 1

    # Process the data to get the list of symptoms
    docs = []
    filter_df = []
    for i in range(len(df)):
        item = []
        for j in range(len(cols)):
            if df.iloc[i][j] == '1':
                item.append(cols[j])
        if(item[-1] == input_age and item[-2] == input_gender):
            docs.append(','.join(item[:-2]))
            filter_df.append(data.iloc[i]['disease'])
    
    # Compute the TF-IDF values for input symptoms
    input_vector = cv.transform(input_symptoms)
    input_tfidf = tfidf_transformer.transform(input_vector)

    # Find the top k diseases
    distances, indices = knn_model.kneighbors(input_tfidf, n_neighbors=k)

    top_diseases = []
    for i in indices[0]:
        top_diseases.append(filter_df[i])

    # Get top 10 symptoms related to the predicted diseases
    all_symptoms = []
    for i in indices[0]:
        symp = docs[i].split(',')
        tempSymp = [s for s in symp if s not in input_symptoms]
        tempSymp = [s for s in tempSymp if s not in rejected_symptoms]
        all_symptoms += tempSymp

    counts = Counter(all_symptoms)
    sorted_symptoms = sorted(counts, key=counts.get)
    
    return jsonify({
        'top_diseases': top_diseases,
        'top_symptoms': sorted_symptoms
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)