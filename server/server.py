from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/')
def get_location_names():#funtion to return all locations
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin',"*")

    return response

@app.route('/', methods=['GET','POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimate_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    return response

if __name__ == '__main__':
    print("Starting Python Falsk Server for home price Prediction...")
    app.run()