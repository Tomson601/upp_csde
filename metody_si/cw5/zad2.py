# Wykorzystując zbiór danych CIFAR-100 oraz model Sequential z biblioteki
# Keras (TensorFlow), zaprojektuj, zaimplementuj i wytrenuj konwolucyjną
# sieć neuronową zdolną do klasyfikacji obrazów na 100 różnych klas. Twoim
# celem jest osiągnięcie jak najlepszej dokładności na zbiorze testowym
# poprzez eksperymentowanie z różnymi architekturami sieci (tzn. z różnymi
# rozmiarami filtrów, liczbą neuronów, głębokością sieci).
import tensorflow as tf


def build_model():
	return tf.keras.Sequential([
		tf.keras.layers.Input(shape=(32, 32, 3)),
		tf.keras.layers.Conv2D(32, 3, activation="relu", padding="same"),
		tf.keras.layers.BatchNormalization(),
		tf.keras.layers.Conv2D(32, 3, activation="relu", padding="same"),
		tf.keras.layers.MaxPooling2D(),
		tf.keras.layers.Dropout(0.25),
		tf.keras.layers.Conv2D(64, 3, activation="relu", padding="same"),
		tf.keras.layers.BatchNormalization(),
		tf.keras.layers.Conv2D(64, 3, activation="relu", padding="same"),
		tf.keras.layers.MaxPooling2D(),
		tf.keras.layers.Dropout(0.35),
		tf.keras.layers.Conv2D(128, 3, activation="relu", padding="same"),
		tf.keras.layers.BatchNormalization(),
		tf.keras.layers.GlobalAveragePooling2D(),
		tf.keras.layers.Dense(256, activation="relu"),
		tf.keras.layers.Dropout(0.5),
		tf.keras.layers.Dense(100, activation="softmax"),
	])


def main():
	(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar100.load_data()
	x_train = x_train.astype("float32") / 255.0
	x_test = x_test.astype("float32") / 255.0

	model = build_model()
	model.compile(
		optimizer=tf.keras.optimizers.Adam(1e-3),
		loss="sparse_categorical_crossentropy",
		metrics=["accuracy"],
	)

	model.fit(
		x_train,
		y_train,
		validation_split=0.1,
		epochs=50,
		batch_size=64,
		callbacks=[
			tf.keras.callbacks.ReduceLROnPlateau(patience=3, factor=0.5),
			tf.keras.callbacks.EarlyStopping(patience=7, restore_best_weights=True),
		],
		verbose=0,
	)

	model.evaluate(x_test, y_test, verbose=0)


if __name__ == "__main__":
	main()
