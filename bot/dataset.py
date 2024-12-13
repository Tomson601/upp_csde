import torch
from torch.utils.data import Dataset

class TextDataset(Dataset):
    def __init__(self, file_path, seq_length=128, vocab_size=5000):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.text = file.read()
                if len(self.text) == 0:
                    raise ValueError(f"The file {file_path} is empty.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} was not found.")
        except ValueError as e:
            raise e

        self.seq_length = seq_length
        self.vocab_size = vocab_size

        # Dodajemy '\n' do mapowania znaków
        self.char_to_idx = {chr(i): i for i in range(32, 127)}
        self.char_to_idx['\n'] = len(self.char_to_idx)  # Dodanie '\n' do mapowania

        # Tworzymy odwrotne mapowanie dla wygody
        self.idx_to_char = {i: chr(i) for i in range(32, 127)}
        self.idx_to_char[len(self.char_to_idx) - 1] = '\n'  # Zmieniamy odwrotne mapowanie dla '\n'

        print(f"Text loaded (first 500 chars): {self.text[:500]}")
        print(f"Text length before trimming: {len(self.text)}")

        # Sprawdzamy, czy długość tekstu jest wystarczająca do wygenerowania próbek
        if len(self.text) < self.seq_length:
            raise ValueError(f"Text length is too short for the specified seq_length ({self.seq_length}).")

        # Przycinamy tekst do najbliższej wielokrotności seq_length
        self.text = self.text[:len(self.text) // self.seq_length * self.seq_length]

        print(f"Text length after trimming: {len(self.text)}")

    def __len__(self):
        num_samples = len(self.text) // self.seq_length
        print(f"Number of samples in dataset: {num_samples}")  # Debugging line
        return num_samples

    def __getitem__(self, idx):
        start_idx = idx * self.seq_length
        end_idx = (idx + 1) * self.seq_length
        sequence = self.text[start_idx:end_idx]
        
        # Konwertowanie na indeksy
        input_seq = torch.tensor([self.char_to_idx.get(char, self.char_to_idx['\n']) for char in sequence[:-1]], dtype=torch.long)
        target_seq = torch.tensor([self.char_to_idx.get(char, self.char_to_idx['\n']) for char in sequence[1:]], dtype=torch.long)

        return input_seq, target_seq
