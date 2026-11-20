# 🎓 Student Placement Predictor

A Machine Learning-based web application that predicts student placement outcomes using **Logistic Regression and Python**.

The system analyzes student-related factors such as academic performance, aptitude, technical skills, communication skills, internships, and projects to predict placement outcomes.

## 🚀 Project Overview

The Student Placement Predictor is designed to demonstrate how Machine Learning can be used to analyze student information and estimate placement outcomes.

It provides an interactive web interface where users can enter student details and get a placement prediction.

## ✨ Features

- Student placement prediction using Machine Learning
- Logistic Regression classification algorithm
- Interactive web interface using Streamlit
- Pre-trained Machine Learning model
- Student dataset for model training
- Model retraining support
- Simple and user-friendly interface

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Pandas | Data Handling |
| NumPy | Numerical Operations |
| Scikit-learn | Machine Learning |
| Logistic Regression | Prediction Algorithm |
| Streamlit | Web Application Interface |

## 📂 Project Structure

```text
Student-Placement-Predictor/
│
├── app.py
├── dataset.csv
├── placement_model.pkl
├── train_model.py
├── requirements.txt
├── run_project.bat
├── README.md
└── VIVA_NOTES.md
```

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

**Step 1: Clone the repository**

```bash
git clone https://github.com/mkumaramit2158-web/student-placement-predictor.git
```

**Step 2: Open the project folder**

```bash
cd student-placement-predictor
```

**Step 3: Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**Step 4: Run the application**

```bash
python -m streamlit run app.py
```

**Step 5: Open the application**

The application will open in your browser. Enter student details and click on the prediction button.

## 🧠 Machine Learning Model

- Algorithm: Logistic Regression
- Learning Type: Supervised Learning
- Problem Type: Classification
- Dataset: Sample student placement dataset

The project includes a pre-trained model. You can also retrain it using:

```bash
python train_model.py
```

## 📊 Dataset & Model Evaluation

The project uses synthetic demonstration data for training and testing.

The reported test accuracy is **84.29%** on a held-out portion of this synthetic dataset. This result does not represent validated real-world placement prediction performance.

## 🎯 Project Objectives

- Understand the practical implementation of Machine Learning.
- Apply classification techniques to student placement data.
- Build an interactive prediction application.
- Gain practical experience with Python and Scikit-learn.

## 🔮 Future Improvements

- Use a larger real-world student placement dataset.
- Experiment with additional classification algorithms.
- Improve model evaluation and prediction reliability.
- Deploy the application online.
- Add data visualization and performance analysis.

## 👨‍💻 Author

**Amit Kumar**

Student | Computer Science & Engineering

GitHub: [@mkumaramit2158-web](https://github.com/mkumaramit2158-web)

## 📜 License

This project is created for educational and academic purposes.

---

⭐ If you find this project useful, consider giving it a star!
