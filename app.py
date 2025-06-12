from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open('diabetes-prediction-rfc-model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        prediction = model.predict(data)
        if prediction == 1: result = "You are likely Diabetic." 
        else: result = "You are likely Not Diabetic."   
        return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
