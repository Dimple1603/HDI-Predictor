# 🌍 Human Development Index (HDI) Predictor

A Machine Learning based web application that predicts the Human Development Index (HDI) of a country using socio-economic indicators such as Life Expectancy, Expected Years of Schooling, Mean Years of Schooling, and Gross National Income (GNI) per Capita.

---

## 📌 Project Overview

The Human Development Index (HDI) is a statistical measure developed by the United Nations Development Programme (UNDP) to evaluate the overall development of a country.

This project uses **Linear Regression** to predict the HDI score based on key development indicators and provides the corresponding human development category.

---

## 🚀 Features

- Predicts Human Development Index (HDI)
- User-friendly Flask web interface
- Machine Learning model using Linear Regression
- Data preprocessing and cleaning
- Displays predicted HDI score
- Classifies countries into Human Development categories

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- HTML
- CSS

---

## 📂 Project Structure

```
HDI-Predictor/
│
├── dataset/
│   └── Human Development Index and Components.csv
│
├── model/
│   └── hdi_model.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Dimple1603/HDI-Predictor.git
```

### Navigate to the project

```bash
cd HDI-Predictor
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Train the model

```bash
python train_model.py
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📊 Input Parameters

- Life Expectancy
- Expected Years of Schooling
- Mean Years of Schooling
- Gross National Income (GNI) Per Capita

---

## 📈 Output

The application predicts:

- HDI Score
- Human Development Category
  - Very High Human Development
  - High Human Development
  - Medium Human Development
  - Low Human Development

---

## 📸 Application Preview

### Home Page

*(Add Screenshot Here)*

### Prediction Result

*(Add Screenshot Here)*

---

## 🔮 Future Enhancements

- Improve prediction accuracy using larger datasets
- Support multiple Machine Learning algorithms
- Interactive data visualization
- Country-wise comparison dashboard
- Deploy the application online

---

## 👨‍💻 Author

**Jagili Dimple Kumar**

B.Tech – Artificial Intelligence & Machine Learning

Mohan Babu University

---

## 📄 License

This project is developed for educational purposes as part of the APSCHE AI & ML Virtual Internship.