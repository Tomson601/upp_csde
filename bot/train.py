import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from model.gpt_model import GPTModel
from model.positional_encoding import PositionalEncoding
from dataset import TextDataset
import numpy as np
from torch.nn import functional as F

# Hyperparameters
batch_size = 64
lr = 0.001
epochs = 10
early_stopping_patience = 3  # Early stopping patience
validation_split = 0.1  # 10% danych jako zbiór walidacyjny

def load_data():
    # Ścieżka do pliku z danymi
    train_dataset = TextDataset('data/sample_data1.txt', seq_length=32)

    print(f"Number of samples in train dataset: {len(train_dataset)}")  # Debugging line

    # Zwracanie DataLoaderów
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    return train_loader  # Zwracamy tylko train_loader, bo nie chcemy używać walidacji

# Train function
def train(model, train_loader, optimizer, criterion, device):
    best_val_loss = float('inf')
    epochs_without_improvement = 0

    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        
        for i, (inputs, targets) in enumerate(train_loader):
            inputs, targets = inputs.to(device), targets.to(device)

            optimizer.zero_grad()
            output = model(inputs)
            loss = criterion(output.view(-1, output.size(-1)), targets.view(-1))
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
        
        # Calculate average loss for the epoch
        epoch_loss = running_loss / len(train_loader)
        print(f'Epoch {epoch + 1}, Loss: {epoch_loss:.4f}')

        # Brak walidacji - usuwamy tę część, jeśli używamy tylko danych treningowych

        # Early stopping check
        if epoch_loss < best_val_loss:
            best_val_loss = epoch_loss
            epochs_without_improvement = 0
        else:
            epochs_without_improvement += 1
            if epochs_without_improvement >= early_stopping_patience:
                print(f'Early stopping at Epoch {epoch + 1}')
                break

# Main training loop
def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load data
    train_loader = load_data()  # Zmieniamy, by ładować tylko dane treningowe

    # Initialize model
    model = GPTModel(vocab_size=5000, d_model=256, nhead=8, num_layers=6, dim_feedforward=512)
    model = model.to(device)

    # Loss function and optimizer
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    # Start training
    train(model, train_loader, optimizer, criterion, device)  # Usuwamy walidację z argumentów

if __name__ == '__main__':
    main()
