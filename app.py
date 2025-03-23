from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load Model
model = BertForSequenceClassification.from_pretrained("customer_service_model")
tokenizer = BertTokenizer.from_pretrained("customer_service_model")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to the specific origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],  # Adjust this to the specific methods you want to allow
    allow_headers=["*"],  # Adjust this to the specific headers you want to allow
)

class QueryRequest(BaseModel):
    text: str

@app.post("/predict")
def predict(request: QueryRequest):
    # Tokenize input text
    inputs = tokenizer(request.text, return_tensors="pt", truncation=True, padding=True, max_length=128).to(device)
    outputs = model(**inputs)

    # Get category prediction
    category_idx = torch.argmax(outputs.logits, dim=1).item()
    
    # Simulated label mapping (Replace with actual label names)
    categories = ["account_issue", "order_issue", "technical_support", "service_issue", "refund", "billing", "subscription"]
    sentiments = ["positive", "neutral", "negative"]
    urgency_levels = ["low", "medium", "high"]
    resolution_statuses = ["pending", "unresolved", "resolved"]

    # Example logic: (You should replace this with your model's actual outputs)
    predicted_category = categories[category_idx % len(categories)]
    predicted_sentiment = sentiments[category_idx % len(sentiments)]
    predicted_urgency = urgency_levels[category_idx % len(urgency_levels)]
    predicted_status = resolution_statuses[category_idx % len(resolution_statuses)]

    return {
        "category": predicted_category,
        "label": predicted_category,  # Assuming category and label are the same
        "sentiment": predicted_sentiment,
        "urgency": predicted_urgency,
        "resolution_status": predicted_status
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)