# 💼 Data Science Salary Estimator

## 📌 Project Overview

This project builds a machine learning model to estimate data science salaries based on job listings. The goal is to help data professionals better understand and negotiate their compensation.

* 📊 Achieved **Mean Absolute Error (MAE) ≈ $11K**
* 🧠 Built multiple ML models and optimized using GridSearchCV
* 🔄 Implemented a **scikit-learn Pipeline** for end-to-end preprocessing and prediction
* 🌐 Deployed using a **Flask API**

---

## 🚀 Key Features

* Used a **Glassdoor jobs dataset from Kaggle**
* Performed extensive **data cleaning and feature engineering**
* Built and optimized:

  * Linear Regression
  * Lasso Regression
  * Random Forest (Best Performer)
* Integrated preprocessing + model using **Pipeline**
* Developed a **Flask API** for real-time predictions

---

## 🛠️ Tech Stack

* **Python Version:** 3.10
* **Libraries:**
  * pandas
  * numpy
  * scikit-learn
  * matplotlib
  * seaborn
  * flask
  * json
  * pickle

---

## 📊 Dataset

* Source: **Kaggle (Glassdoor Job Listings Dataset)**
* Contains job-level data such as:

  * Job Title
  * Salary Estimate
  * Job Description
  * Rating
  * Company Info (Size, Industry, Sector, Revenue)
  * Location

---

## 🧹 Data Cleaning & Feature Engineering

Key transformations:

* Extracted numeric salary values
* Identified hourly vs employer-provided salaries
* Removed entries without salary data
* Parsed company ratings
* Derived company **state** and **headquarter flag**
* Converted founding year → company age
* Extracted skill-based features from job descriptions:

  * Python
  * R
  * Excel
  * AWS
  * Spark
* Created:

  * Simplified job title
  * Seniority level
  * Job description length

---

## 📊 Exploratory Data Analysis (EDA)

* Analyzed distributions of salary and ratings
* Explored categorical variables using pivot tables
* Identified trends in:

  * Industry vs salary
  * Job role vs compensation
  * Skill demand
 
<img width="186" height="268" alt="image" src="https://github.com/user-attachments/assets/851036ce-15e1-4dca-8396-dfb8e8063f0c" />
<img width="390" height="255" alt="image" src="https://github.com/user-attachments/assets/0d950f7c-069e-4566-9a17-0a1d87ef5ffd" />
<img width="345" height="293" alt="image" src="https://github.com/user-attachments/assets/0c667a97-9b29-49f8-b218-30f2936802db" />

---

## 🤖 Model Building

### Data Preparation

* Used **raw dataset (no manual encoding)**
* Split dataset:

  * **Train: 80%**
  * **Test: 20%**

---

### 🔄 Pipeline Architecture (Key Enhancement)

To ensure scalability and avoid manual feature handling, a **Pipeline** was implemented:

```python
Pipeline(
    steps=[
        ('preprocessor', ColumnTransformer([
            ('num', StandardScaler(), num_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols),
            ('bin', 'passthrough', bin_cols)
        ])),
        ('model', RandomForestRegressor())
    ]
)
```

👉 Benefits:

* Eliminates need for manual encoding (`get_dummies`)
* Ensures consistent preprocessing during training and inference
* Prevents feature mismatch errors
* Makes deployment cleaner and production-ready

---

### Models Used

| Model             | Purpose               |
| ----------------- | --------------------- |
| Linear Regression | Baseline              |
| Lasso Regression  | Handle sparsity       |
| Random Forest     | Capture non-linearity |

---

## 📈 Model Performance

| Model             | MAE       |
| ----------------- | --------- |
| Random Forest     | **11.22** |
| Linear Regression | 18.86     |
| Ridge Regression  | 19.67     |

👉 **Random Forest performed best**

---

## ⚙️ Model Optimization

Used **GridSearchCV** to tune:

* Number of estimators
* Splitting criteria
* Feature selection

---

## 🌐 Productionization (Flask API)

A Flask API was built to serve predictions using the trained pipeline.

### 🔄 Pipeline Integration in Deployment

Instead of passing preprocessed features, the API accepts **raw input data**:

```python
pipeline = pickle.load(open("models/pipeline.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = pipeline.predict(df)[0]
    return jsonify({'prediction': float(prediction)})
```

👉 This ensures:

* Same preprocessing as training
* No manual feature engineering in API
* Robust and scalable inference

---

### API Endpoint

```http
POST /predict
```

### Input Example

```json
{
  "Rating": 3.6,
  "age": 34,
  "desc_len": 4608,
  "num_comp": 1,
  "Size": "1001 to 5000 employees",
  "Industry": "Biotech & Pharmaceuticals",
  "Sector": "Healthcare",
  "Revenue": "$1 to $5 billion (USD)",
  "job_state": "CA",
  "python_yn": 1,
  "spark": 0,
  "excel": 1
}
```

### Output

```json
{
  "prediction": 110.795
}
```

---

## 📁 Project Structure

```bash
.
├── FlaskAPI/
│   ├── app.py
│   ├── data_input.py
│   ├── New.py
│   ├── models/
│   │   ├── pipeline.pkl
│   │   └── model_file.p
│   ├── wsgi.py
│   └── venv/
│
├── notebooks/
├── data/
├── requirements.txt
└── README.md
```

---

## 🔥 Future Improvements

* Deploy API to cloud (Render / AWS / Railway)
* Add frontend UI for user input
* Improve model with XGBoost / LightGBM
* Add real-time data integration

---

## 👤 Author

**Zaid Shaikh**

---

## ⭐ Acknowledgements

* Kaggle dataset contributors
* scikit-learn documentation
* Flask community

---
