import torch
from model.gpt_model import GPTModel

# Parametry modelu
vocab_size = 10
d_model = 128
nhead = 4
num_layers = 2
dim_feedforward = 256
max_len = 50

model = GPTModel(vocab_size, d_model, nhead, num_layers, dim_feedforward, max_len)
model.load_state_dict(torch.load("gpt_model.pth"))  # Załaduj zapisany model

# Słownik
word2idx = {"hello": 2, "world": 3, "<pad>": 0, "<unk>": 1}
idx2word = {v: k for k, v in word2idx.items()}

# Generowanie
def generate(prompt, max_length=10):
    input_ids = torch.tensor([word2idx.get(word, 1) for word in prompt.split()])
    for _ in range(max_length):
        logits = model(input_ids.unsqueeze(0))
        next_token = logits.argmax(dim=-1)[:, -1]
        input_ids = torch.cat((input_ids, next_token))
    return " ".join([idx2word.get(idx, "<unk>") for idx in input_ids.tolist()])

print(generate("hello"))
