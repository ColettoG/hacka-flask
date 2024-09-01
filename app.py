from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from model import main

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    y_pred = main()
    print(y_pred)
    return jsonify(f"message: {y_pred}")
    
if __name__ == '__main__':
    app.run(debug=True)
