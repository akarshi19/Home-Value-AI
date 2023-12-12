import pandas as pd
from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
data = pd.read_csv('Delhi3.csv')
pipe = pickle.load(open("LinearRegressionModel1.pk", 'rb'))


@app.route('/')
def index():

    Addresses = sorted(data['Address'].unique())
    return render_template('predict.html', Addresses = Addresses)


@app.route('/predict',methods=['POST'])
def predict():
    Address = request.form.get('Address')
    area = request.form.get('area')
    Bedrooms = request.form.get('Bedrooms')
    print(Address, area, Bedrooms)
    input = pd.DataFrame([[Address, area, Bedrooms]], columns=['Address', 'area', 'Bedrooms'])
    prediction = pipe.predict(input)[0]
    print(prediction)


    return str(np.round(prediction,3))

    return ""

    


if __name__ == "__main__":
    app.run(debug=True, port=5000)
