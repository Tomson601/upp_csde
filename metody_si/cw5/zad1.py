# Wykorzystaj zbiór MNIST w dataset do zaprojektowania sieci
# konwolucyjnej (CNN).
# Zwiększ liczbę warstw i porównaj wyniki (3 różne modele).
# Oblicz pozostałe met ryki wykorzystując moduły dla loss i metrics:
#   a.from keras.losses import mean_squared_error, mean_absolute_error
#   b.from keras.metrics import mean_absolute_percentage_error
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from tensorflow.keras.losses import mean_absolute_error, mean_squared_error
from tensorflow.keras.metrics import mean_absolute_percentage_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical


(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = (x_train.astype("float32") / 255.0)[..., None]
x_test = (x_test.astype("float32") / 255.0)[..., None]
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


def build_model(extra_conv_layers):
	model = Sequential([Conv2D(16, (3, 3), activation="relu", input_shape=(28, 28, 1)), MaxPooling2D((2, 2))])
	for filters in extra_conv_layers:
		model.add(Conv2D(filters, (3, 3), activation="relu"))
		model.add(MaxPooling2D((2, 2)))
	model.add(Flatten())
	model.add(Dense(64, activation="relu"))
	model.add(Dense(10, activation="softmax"))
	model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
	return model


configs = {
	"model_1": [],
	"model_2": [32],
	"model_3": [32, 64],
}

for name, extra_conv_layers in configs.items():
	model = build_model(extra_conv_layers)
	model.fit(x_train[:10000], y_train[:10000], epochs=3, batch_size=64, verbose=0)
	loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
	y_pred = model.predict(x_test, verbose=0)
	print(f"{name}: loss={loss:.4f}, accuracy={accuracy:.4f}")
	print(f"  mse={mean_squared_error(y_test, y_pred).numpy().mean():.4f}")
	print(f"  mae={mean_absolute_error(y_test, y_pred).numpy().mean():.4f}")
	print(f"  mape={mean_absolute_percentage_error(y_test, y_pred).numpy().mean():.4f}")
