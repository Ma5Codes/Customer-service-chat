# train.py
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import BertForSequenceClassification
from torch.optim import AdamW
from preprocess import train_encodings, train_labels, val_encodings, val_labels, tokenizer

class CustomerServiceDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return {
            'input_ids': torch.tensor(self.encodings['input_ids'][idx]),
            'attention_mask': torch.tensor(self.encodings['attention_mask'][idx]),
            'labels': torch.tensor(self.labels[idx])
        }

# Convert to PyTorch Dataset
train_dataset = CustomerServiceDataset(train_encodings, train_labels)
val_dataset = CustomerServiceDataset(val_encodings, val_labels)

# Load Model
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(set(train_labels)))
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# DataLoader
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=16, shuffle=False)

# Optimizer
optimizer = AdamW(model.parameters(), lr=5e-5)

# Training Loop
for epoch in range(2):  # Run for 2 epochs
    model.train()
    for batch in train_loader:
        optimizer.zero_grad()
        input_ids, attention_mask, labels = batch['input_ids'].to(device), batch['attention_mask'].to(device), batch['labels'].to(device)
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
    print(f"✅ Epoch {epoch+1} completed!")

# Save Model
model.save_pretrained("customer_service_model")
tokenizer.save_pretrained("customer_service_model")

print("✅ Model Training Done! Run 'evaluate.py' next.")