# ❤️ Heart Disease Prediction using Machine Learning

## 📌 Project Overview
This project predicts whether a person has heart disease based on medical parameters using Machine Learning. The web-based interface is built using **Streamlit**, and the model is trained using **scikit-learn**.

## 🚀 Features
- Machine Learning model trained on a heart disease dataset.
- User-friendly web interface built with **Streamlit**.
- Takes various medical inputs and provides a prediction.
- Can be deployed on **Streamlit Cloud**, **Heroku**, or **AWS**.

## 🛠️ Installation & Setup
Set Up Virtual Environment (macOS/Linux)
- python3 -m venv env
- source env/bin/activate

For Windows:
- python -m venv env
- env\Scripts\activate

Install Dependencies
streamlit
scikit-learn
numpy
pandas
matplotlib
seaborn
joblib

Running the Project
1. Train the Model (If Not Already Saved)
python train_model.py

Run the Web App
streamlit run app.py

📊 Dataset Information
The dataset includes key medical parameters such as:

Age
Sex
Chest Pain Type (cp)
Resting Blood Pressure (trestbps)
Serum Cholesterol (chol)
Fasting Blood Sugar (fbs)
Resting ECG (restecg)
Maximum Heart Rate Achieved (thalach)
Exercise Induced Angina (exang)
ST Depression (oldpeak)
Slope of Peak Exercise ST Segment
Number of Major Vessels Colored by Fluoroscopy
Thalassemia (thal)

🔬 Machine Learning Model
The model uses K-Nearest Neighbors (KNN) for prediction.
Achieved 87% accuracy after hyperparameter tuning.
Uses scikit-learn for training.
🔗 Deployment Options
The app can be deployed using:

Streamlit Cloud → https://share.streamlit.io
Heroku → https://heroku.com
AWS EC2 / Lambda
🖥️ Tech Stack
Frontend: Streamlit
Backend: Python, Flask (Optional)

Machine Learning: Scikit-learn
Deployment: Streamlit Cloud / Heroku
📷 Screenshots
Home Page	Prediction Page

![image](https://github.com/user-attachments/assets/0e4a6426-8717-4ac2-8165-aae581435f6d)

![image](https://github.com/user-attachments/assets/db3da1da-353b-4c7f-9657-586f437ff51e)

![image](https://github.com/user-attachments/assets/672e8a68-1139-438e-a2e3-bf66e057b2ea)



✨ Future Improvements
Train the model with a larger dataset.
Improve accuracy with Deep Learning (TensorFlow/Keras).
Deploy using Flask API.
💡 Contributing
Contributions are welcome! Feel free to submit a pull request.

📜 License
This project is licensed under the MIT License.

📞 Contact
For queries or suggestions:

✉️ Email: nikhilhalle7711@gmail.com
🔗 GitHub: @NikhilHalle
