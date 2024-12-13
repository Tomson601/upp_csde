import torch
import torch.nn as nn
from model.positional_encoding import PositionalEncoding
from model.transformer_decoder import TransformerDecoderBlock

class GPTModel(nn.Module):
    def __init__(self, vocab_size, d_model=512, nhead=8, num_layers=6, dim_feedforward=2048, max_len=5000, dropout=0.1):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoder = PositionalEncoding(d_model, max_len)
        self.layers = nn.ModuleList([TransformerDecoderBlock(d_model, nhead, dim_feedforward, dropout) for _ in range(num_layers)])
        self.fc_out = nn.Linear(d_model, vocab_size)
        
    def forward(self, x):
        x = self.embedding(x) * (x.size(-1) ** 0.5)
        x = self.pos_encoder(x)
        for layer in self.layers:
            x = layer(x)
        logits = self.fc_out(x)
        return logits
