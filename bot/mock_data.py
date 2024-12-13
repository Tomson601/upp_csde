import random

# Lista przykładowych zdań do generowania danych
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Artificial intelligence is transforming the world.",
    "Deep learning models are capable of learning from vast amounts of data.",
    "The future of AI looks promising with advancements in natural language processing.",
    "I enjoy reading books and learning new things every day.",
    "Python is a popular programming language in data science and machine learning.",
    "The weather today is sunny with a few clouds in the sky.",
    "Machine learning algorithms require a large amount of data to be effective.",
    "Data preprocessing is an important step in building machine learning models.",
    "Natural language processing helps computers understand human language.",
    "Artificial intelligence can be applied in healthcare, finance, and education.",
    "The advancements in quantum computing could revolutionize technology.",
    "Big data is changing the way we make decisions and understand the world.",
    "IoT (Internet of Things) connects devices to improve efficiency and data sharing.",
    "Blockchain technology ensures secure and transparent transactions.",
    "Neural networks are the backbone of deep learning models.",
    "Self-driving cars are being developed by various companies around the world.",
    "The stock market is influenced by various global economic factors.",
    "Cybersecurity is a growing concern in the digital age.",
    "Robotic process automation is streamlining business operations."
]

# Zmienna przechowująca dane
data = []

# Generujemy dane tekstowe, które łącznie będą miały około 150 MB
target_size_in_bytes = 225 * 1024 * 1024  # 150 MB w bajtach
current_size_in_bytes = 0

# Powtarzaj tekst aż osiągniesz odpowiednią objętość
while current_size_in_bytes < target_size_in_bytes:
    sentence = random.choice(sentences)
    data.append(sentence)
    current_size_in_bytes += len(sentence.encode('utf-8'))  # Rozmiar w bajtach

# Zapisz dane do pliku
with open('data/sample_data1.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(data))

print("Plik 'sample_data1.txt' został wygenerowany!")
