# evaluate.py
from sklearn.metrics import accuracy_score
import torch
import preprocess
from torch.utils.data import DataLoader
from transformers import BertForSequenceClassification

# Load Model
model = BertForSequenceClassification.from_pretrained("customer_service_model")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Create validation DataLoader
val_dataset = preprocess.CustomerServiceDataset(preprocess.val_encodings, preprocess.val_labels)
val_loader = DataLoader(val_dataset, batch_size=16, shuffle=False)

# Evaluation Function
def evaluate(model, val_loader):
    model.eval()
    predictions, true_labels = [], []
    with torch.no_grad():
        for batch in val_loader:
            input_ids, attention_mask, labels = (
                batch['input_ids'].to(device),
                batch['attention_mask'].to(device),
                batch['labels'].to(device),
            )
            outputs = model(input_ids, attention_mask=attention_mask)
            preds = torch.argmax(outputs.logits, dim=1).cpu().numpy()
            predictions.extend(preds)
            true_labels.extend(labels.cpu().numpy())
    
    acc = accuracy_score(true_labels, predictions)
    print(f"✅ Validation Accuracy: {acc:.4f}")

# Run evaluation
evaluate(model, val_loader)
