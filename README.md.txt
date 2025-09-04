# 📩 Spam Classifier API

A simple API to detect whether a text is **spam** or **not spam**, using a classic Machine Learning model (NLP).  
This project is containerized with **Docker** and ready to be deployed on **Render**.

---

## 🎯 Project Goals
- Build an API for spam text classification.
- Learn the workflow of **deploying ML models** into production.
- Practice using **Docker** and **Render** for cloud deployment.

---

## 📂 Project Structure
spam_api/
│-- app.py # Main API (Flask)
│-- Dockerfile # Docker configuration
│-- requirements.txt # Dependencies
│-- spam_classifier.pkl # Trained ML model
│-- README.md # Project documentation


---

## ⚙️ Local Setup & Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/<username>/spam-classifier-api.git
   cd spam-classifier-api

2. **Clone the repository**
pip install -r requirements.txt

3. **Run the API**
python app.py

API will be running at:
👉 http://localhost:5000

🐳 Run with Docker (Local)

Build the image

docker build -t spam-classifier-api .


Run the container

docker run -p 5000:5000 spam-classifier-api


Test the API

curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{"text": "Free money now!!!"}'


Example response:

{
  "prediction": "spam"
}

🚀 Deployment on Render

Push the project to GitHub.

Go to Render Dashboard
.

Select New > Web Service.

Connect to this GitHub repository.

For Environment, choose Docker.

Deploy → Render will automatically build and run the container.

📌 Endpoints

POST /predict
Request body:

{
  "text": "your message here"
}


Response:

{
  "prediction": "spam" | "not spam"
}

🛠️ Tech Stack

Python 3.9

Flask

Scikit-learn

Docker

Render

✍️ Built by Carmenita Lamba – as a practice project for NLP Model Deployment 🚀


---