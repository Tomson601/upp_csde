import torch
from model.gpt_model import GPTModel
from dataset import TextDataset
import numpy as np
from torch.nn import functional as F

# Załaduj wytrenowany model
def load_model():
    model = GPTModel(vocab_size=5000, d_model=256, nhead=8, num_layers=6, dim_feedforward=512)
    model.load_state_dict(torch.load('model.pth'))  # Załaduj zapisany model
    model.eval()  # Ustaw model w tryb ewaluacji
    return model

# Funkcja do generowania odpowiedzi przez model
def generate_response(model, input_text, seq_length=32):
    # Przekształć tekst wejściowy na dane wejściowe dla modelu
    input_ids = [ord(char) for char in input_text]  # Możesz dostosować tę konwersję, w zależności od używanego tokenizera
    input_ids = torch.tensor(input_ids).unsqueeze(0)  # Dodaj wymiar partii (batch dimension)
    
    # Wykorzystaj model do przewidywania
    with torch.no_grad():
        output = model(input_ids)
        predicted_ids = output.argmax(dim=-1)  # Pobierz najbardziej prawdopodobne tokeny
        
    # Przekształć wynik na tekst
    response = ''.join([chr(id.item()) for id in predicted_ids[0]])
    return response

# Funkcja interakcji z użytkownikiem
def chat():
    model = load_model()
    print("Bot jest gotowy do rozmowy! (Aby zakończyć, wpisz 'quit')")
    
    while True:
        user_input = input("Ty: ")
        
        if user_input.lower() == 'quit':
            print("Bot: Do zobaczenia!")
            break
        
        # Generuj odpowiedź na podstawie wejścia użytkownika
        bot_response = generate_response(model, user_input)
        print(f"Bot: {bot_response}")

if __name__ == '__main__':
    chat()
