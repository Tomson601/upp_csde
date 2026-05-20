from tensorflow import keras
from tensorflow.keras import layers, models

# Ładowanie i przygotowanie danych
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train = x_train.reshape((-1, 28, 28, 1))
x_test = x_test.reshape((-1, 28, 28, 1))

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

n_train = min(2000, x_train.shape[0])
n_test = min(1000, x_test.shape[0])
x_train_small, y_train_small = x_train[:n_train], y_train[:n_train]
x_test_small, y_test_small = x_test[:n_test], y_test[:n_test]
epochs = 1

model.fit(x_train_small, y_train_small, epochs=epochs, batch_size=128, verbose=2)

test_loss, test_acc = model.evaluate(x_test_small, y_test_small, verbose=2)


print('Podsumowanie')
print(f'Wynik (test accuracy): {test_acc:.4f}')
print(f'Wynik (test loss): {test_loss:.4f}')
print('Liczba warstw Conv2D: 1')
print(f'Wejście: {model.input_shape[1:]}')
print(f'Wyjście: {model.output_shape[-1]}')
print(f'Liczba epok użytych do treningu: {epochs}')
