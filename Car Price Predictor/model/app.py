import pickle
from flask_cors import CORS
from flask import Flask, request, jsonify
import numpy as np
import pandas as pd

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "https://ml2024.vercel.app"}})
car = pd.read_csv('cleaned_data.csv')
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

@app.route('/api/data', methods=['GET'])
def get_data():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].astype(int).unique(), reverse=True)
    fuel_types = car['fuel_type'].unique().tolist()
    
    return jsonify({
        'companies': companies,
        'car_models': car_models,
        'years': list(map(int, years)),
        'fuel_types': fuel_types
    })

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        company = data.get('company')
        year = int(data.get('year'))
        driven = int(data.get('kilo_driven'))
        fuel_type = data.get('fuel_type')
        car_model = data.get('car_models')

        prediction = model.predict(pd.DataFrame([[0, car_model, company, year, driven, fuel_type]], 
                                                columns=['Unnamed: 0', 'name', 'company', 'year', 'kms_driven', 'fuel_type']))
        
        return jsonify({'prediction': np.round(prediction[0], 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/')
def index():
    return "Hello, World!"

# if __name__ == "__main__":
#     app.run(debug=True)



# import pickle
# from flask_cors import CORS, cross_origin
# from flask import Flask, render_template, request
# import numpy as np
# import pandas as pd

# app = Flask(__name__)
# cors=CORS(app)
# car = pd.read_csv('cleaned_data.csv')
# model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

# @app.route('/')
# def hello():
#     companies = sorted(car['company'].unique())
#     car_models = sorted(car['name'].unique())
#     years = sorted(car['year'].unique(), reverse = True)
#     fuel_types = car['fuel_type'].unique()
#     return render_template('index.html', companies = companies, car_models = car_models, years = years, fuel_types = fuel_types)

# @app.route('/predict', methods = ['POST'])
# @cross_origin()
# def predict():
#     company = request.form.get('company')
#     year = int(request.form.get('year'))
#     driven = int(request.form.get('kilo_driven'))
#     fuel_type = request.form.get('fuel_type')
#     car_model = request.form.get('car_models')
#     prediction=model.predict(pd.DataFrame([[0,car_model,company,year,driven,fuel_type]],columns=['Unnamed: 0','name', 'company', 'year', 'kms_driven', 'fuel_type']))
#     print(prediction)

#     return str(np.round(prediction[0],2))

# if __name__ == "__main__":
#     app.run(debug=True)