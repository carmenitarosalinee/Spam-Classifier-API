# 📩 Spam Classifier API

A simple Flask-based REST API that classifies text messages as **spam** or **ham (not spam)**.  
The model is built with **Scikit-learn**, serialized with **joblib**, and deployed as a web service using **Gunicorn** and **Docker**.

---

## 📂 Project Structure

Spam-Classifier-API/  
│-- app.py               # Main API code (Flask + model prediction)  
│-- spam_classifier.pkl  # Trained ML model  
│-- requirements.txt     # Python dependencies  
│-- Dockerfile           # Docker image configuration  
│-- Procfile             # Process declaration for deployment  
│-- runtime.txt          # Python runtime version  
│-- README.md            # Project documentation  

---

## 🔑 File Explanations

- **app.py** → Flask API with 2 endpoints:  
  - `/` → Health check (returns API running message)  
  - `/predict` → POST endpoint to classify input text (spam/ham)  

- **spam_classifier.pkl** → Serialized machine learning model (trained beforehand).  

- **requirements.txt** → Dependencies for the API:  
  Flask (API framework), Joblib (load ML model), Pandas (data preprocessing),  
  Scikit-learn (ML model training & prediction), Gunicorn (production WSGI server).  

- **Dockerfile** → Defines containerization process. Uses Python 3.9-slim base image, installs dependencies, copies app + model, exposes port 5000, and runs the app with Gunicorn.  

- **Procfile** → Defines how the app is run in production (`web: gunicorn app:app`).  

- **runtime.txt** → Defines Python runtime version (`python-3.10.12`) for cloud services like Railway/Heroku.  

---

## ⚙️ Local Setup & Run

1. Clone this repository  
   `git clone https://github.com/carmenitarosalinee/Spam-Classifier-API.git`  
   `cd Spam-Classifier-API`  

2. Install dependencies  
   `pip install -r requirements.txt`  

3. Run the API locally  
   `python app.py`  

API will be available at 👉 http://127.0.0.1:5000  

---

## 🐳 Run with Docker

1. Build the Docker image  
   `docker build -t spam-classifier-api .`  

2. Run the container  
   `docker run -p 5000:5000 spam-classifier-api`  

3. Test the API  
   `curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"text": "Free money now!!!"}'`  

**Response:**  
`{ "text": "Free money now!!!", "prediction": "spam" }`  

---

## 📌 API Endpoints

1. **Health Check**  
   GET `/`  
   Response:  
   `{ "message": "Spam Classifier API is running!" }`  

2. **Predict Spam/Ham**  
   POST `/predict`  

   Request body:  
   `{ "text": "Congratulations! You've won a free ticket." }`  

   Response:  
   `{ "text": "Congratulations! You've won a free ticket.", "prediction": "spam" }`  

---

## 🚀 Deployment

This project is ready for deployment on **Railway** or any PaaS that supports **Python + Docker**.  

- `Procfile` ensures Gunicorn runs the Flask app in production.  
- `runtime.txt` specifies the Python version.  
- `Dockerfile` provides a reproducible container setup.  

**Steps (Railway example):**  
1. Push project to GitHub  
2. Create new project in Railway  
3. Connect GitHub repo  
4. Deploy → Railway builds and serves API  

---

## 🛠️ Tech Stack
- Python 3.9 / 3.10  
- Flask  
- Scikit-learn  
- Pandas  
- Joblib  
- Gunicorn  
- Docker  
- Railway (deployment)  

---

## 🙌 Author
Built with ❤️ by **Carmenita**  
