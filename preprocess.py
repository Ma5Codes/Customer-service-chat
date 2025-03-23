# preprocess.py
import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer
import torch
from torch.utils.data import Dataset

# Load dataset (Ensure you have a CSV file named 'customer_service_data.csv')
df = pd.read_csv("customer_service_data.csv")

# Ensure required columns exist
if 'text' not in df.columns or 'label' not in df.columns:
    raise KeyError("Dataset must contain 'text' and 'label' columns.")

# Initialize tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Train-test split
train_texts, val_texts, train_labels, val_labels = train_test_split(
    df['text'].tolist(), df['label'].tolist(), test_size=0.2, random_state=42
)

# Create a label mapping (Convert labels to numerical values)
label_mapping = {label: idx for idx, label in enumerate(set(train_labels))}
train_labels = [label_mapping[label] for label in train_labels]
val_labels = [label_mapping[label] for label in val_labels]

# Tokenize text
train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=128)
val_encodings = tokenizer(val_texts, truncation=True, padding=True, max_length=128)

# Define the Dataset Class
class CustomerServiceDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return {
            'input_ids': torch.tensor(self.encodings['input_ids'][idx], dtype=torch.long),
            'attention_mask': torch.tensor(self.encodings['attention_mask'][idx], dtype=torch.long),
            'labels': torch.tensor(self.labels[idx], dtype=torch.long)
        }

# Make variables accessible
__all__ = ['train_encodings', 'train_labels', 'val_encodings', 'val_labels', 'tokenizer', 'CustomerServiceDataset']

print("✅ Data Preprocessing Done! Run 'train.py' next.")
