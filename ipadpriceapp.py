from crypt import methods
from flask import Flask, request, jsonify, render_template
import flask
import numpy as np
from joblib import load

app = Flask(__name__)

model = load('ipadprice.joblib')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods= ['POST'])
def predict():
    #get values from the browser
    if (request.method == 'POST'):
        int_features = [x for x in request.form.values()]
        final_features = [np.array(int_features)]
        preds = int(model.predict(final_features)[0])
        return render_template('index.html',prediction_text='Predicted Ipad Price is ${}'.format(preds))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.debug=True
    app.run()