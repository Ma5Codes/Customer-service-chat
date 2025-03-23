# 📝 NLP-Based Customer Support Chatbot  

This project is an **NLP-powered customer support chatbot** that categorizes and responds to user queries using **FastAPI** for the backend and a React-based frontend. The model is trained on customer service data to automate responses and improve customer interactions.  

## 🚀 Features  
- **Natural Language Processing (NLP)** – Classifies user queries into predefined categories.  
- **FastAPI Backend** – Handles API requests and serves predictions.  
- **React Frontend** – Provides an intuitive user interface for interacting with the chatbot.  
- **Machine Learning Model** – Custom-trained to understand and categorize customer queries.  
- **Local Testing & Deployment** – Supports testing via `curl` and UI interactions.  

## 📂 Project Structure  
```
📦 NLP Chatbot  
 ┣ 📂 customer_service_model  # Model & NLP assets  
 ┃ ┣ 📜 config.json  
 ┃ ┣ 📜 tokenizer_config.json  
 ┃ ┣ 📜 vocab.txt  
 ┣ 📂 frontend  # React-based UI  
 ┣ 📜 app.py  # FastAPI server  
 ┣ 📜 train.py  # Training script for the NLP model  
 ┣ 📜 test_api.py  # API endpoint testing  
 ┣ 📜 evaluate.py  # Model evaluation  
 ┣ 📜 preprocess.py  # Preprocessing script for text data  
 ┣ 📜 customer_service_data.csv  # Dataset  
```

## 🛠️ Installation & Setup  
### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/your-username/nlp-chatbot.git  
cd nlp-chatbot
```

### 2️⃣ Set Up the Backend  
```sh
cd backend  
python3 -m venv myenv  
source myenv/bin/activate  # (For Linux/macOS)  
myenv\Scripts\activate  # (For Windows)  
pip install -r requirements.txt  
uvicorn app:app --host 0.0.0.0 --port 8000  
```

### 3️⃣ Start the Frontend  
```sh
cd frontend  
npm install  
npm run dev  
```

## 🧪 Testing the API  
You can test the backend using `curl` or Postman:  
```sh
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"text":"How do I reset my password?"}'
```
Expected response:  
```json
{"category": 19}
```

## 📸 Screenshots  
### 🔹 User Interface  
![UI Screenshot](./frontend/public/chatbot_ui.png)  

### 🔹 Folder Structure  
![Project Structure](./project_structure.png)  

## 📌 Future Improvements  
- Improve response accuracy with **LSTM/CNN models**  
- Add **multi-language support**  
- Deploy using **Docker & Kubernetes**  

## 🤝 Contributing  
Feel free to fork the repo and submit a pull request!  

## 📜 License  
MIT License.  
🚀
