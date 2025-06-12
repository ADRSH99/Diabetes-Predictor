
# 🩺 Diabetes Predictor - Machine Learning Web Application

This project is a end-to-end web application for predicting whether a person is diabetic based on clinical input parameters. It combines a trained **Random Forest Classifier**, **Flask** Backend and a Docker-compatible deployment setup.

---

## ✨ Features

-  Machine learning model with **98.75% accuracy**
-  Clean, responsive dark-themed web UI (HTML/CSS with Bootstrap)
-  Flask-based backend API
-  Docker support for easy deployment

---

## 🧠 Machine Learning Model

### 🎯 Model Details

- **Type**: Supervised Classification
- **Algorithm**: `RandomForestClassifier` (from `scikit-learn`)
- **Dataset**: PIMA Indian Diabetes Dataset (`diabetes.csv`)
- **Performance**: 98.75% accuracy on the test set

### 🏗️ Features Used

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### 🛠 Training Steps

1. Dataset loaded and cleaned in a Jupyter notebook
2. Train-test split performed (typically 80-20 or 70-30)
3. Features scaled using `StandardScaler`
4. Trained `RandomForestClassifier` saved using `joblib`
5. Stored as `random_forest_model.pkl` inside the `/training` directory

---

## 🧰 Python Modules Used

- `flask` – Web framework
- `sklearn` – ML model and preprocessing
- `pandas` – Data manipulation
- `numpy` – Numerical operations
- `joblib` – Model serialization
- `wtforms` – Form handling
- `flask-wtf` – Flask extension for WTForms
- `jinja2` – HTML templating engine

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🗂️ Project Structure

```
Diabetes-Predictor/
├── app.py                        # Main Flask application
├── templates/
│   ├── index.html                # Input form UI
│   └── result.html              # Result display page
├── training/
│   ├── diabetes.csv              # Training dataset
│   ├── diabetes_model_rf.ipynb   # Model training notebook
│   └── random_forest_model.pkl   # Trained ML model
├── Dockerfile                    # Docker container config
├── requirements.txt              # Python dependencies
└── README.md
```

---

## 🚀 Running the App Locally

### Prerequisites

- Python 3.8+
- pip

### 🔧 Steps

1. **Clone the repository**

```bash
git clone https://github.com/ADRSH99/Diabetes-Predictor.git
cd Diabetes-Predictor
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages**

```bash
pip install -r requirements.txt
```

4. **Run the Flask server**

```bash
python app.py
```

5. Open your browser and go to:  
   👉 http://localhost:5000

---

## 🐳 Running with Docker

### 🧱 Build Docker Image

```bash
docker build -t diabetes-predictor .
```

### 🚢 Run Docker Container

```bash
docker run -p 5000:5000 diabetes-predictor
```

Then open:  
👉 http://localhost:5000

---

## 📊 Example Input

| Feature                  | Value |
|--------------------------|-------|
| Pregnancies              | 2     |
| Glucose                  | 120   |
| Blood Pressure           | 70    |
| Skin Thickness           | 20    |
| Insulin                  | 85    |
| BMI                      | 33.6  |
| Diabetes Pedigree Function | 0.672 |
| Age                      | 45    |

---

## 🧪 Re-training the Model

1. Open the notebook: `training/diabetes_model_rf.ipynb`
2. Run all cells to train and export `random_forest_model.pkl`
3. Replace the model file in `training/`
4. Restart the Flask app

---
