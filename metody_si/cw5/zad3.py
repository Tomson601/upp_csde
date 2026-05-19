# Wykorzystując zbiór danych SVHN (Street View House Numbers) oraz
# model Sequential z biblioteki Keras (TensorFlow), zaprojektuj,
# zaimplementuj i wytrenuj konwolucyjną sieć neuronową zdolną do
# rozpoznawania cyfr od 0 do 9 na podstawie obrazów wyciętych z Google
# Street View. Twoim celem jest osiągnięcie jak najlepszej dokładności na
# zbiorze testowym.
from __future__ import annotations
import os

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")

import tensorflow as tf
import tensorflow_datasets as tfds

# try:
# 	import tensorflow_datasets as tfds
# except ImportError as exc:  # pragma: no cover
# 	raise SystemExit("Brak biblioteki tensorflow-datasets. Zainstaluj: pip install tensorflow-datasets") from exc


def preprocess(image, label):
	image = tf.cast(image, tf.float32) / 255.0
	label = tf.cast(label, tf.int32)
	return image, label


def build_model():
	data_augmentation = tf.keras.Sequential(
		[
			tf.keras.layers.RandomTranslation(0.08, 0.08),
			tf.keras.layers.RandomRotation(0.08),
			tf.keras.layers.RandomZoom(0.1),
		],
		name="augmentation",
	)

	model = tf.keras.Sequential(
		[
			tf.keras.layers.Input(shape=(32, 32, 3)),
			data_augmentation,
			tf.keras.layers.Conv2D(32, 3, padding="same", activation="relu"),
			tf.keras.layers.BatchNormalization(),
			tf.keras.layers.Conv2D(32, 3, padding="same", activation="relu"),
			tf.keras.layers.BatchNormalization(),
			tf.keras.layers.MaxPooling2D(),
			tf.keras.layers.Dropout(0.25),
			tf.keras.layers.Conv2D(64, 3, padding="same", activation="relu"),
			tf.keras.layers.BatchNormalization(),
			tf.keras.layers.Conv2D(64, 3, padding="same", activation="relu"),
			tf.keras.layers.BatchNormalization(),
			tf.keras.layers.MaxPooling2D(),
			tf.keras.layers.Dropout(0.30),
			tf.keras.layers.Conv2D(128, 3, padding="same", activation="relu"),
			tf.keras.layers.BatchNormalization(),
			tf.keras.layers.MaxPooling2D(),
			tf.keras.layers.Dropout(0.35),
			tf.keras.layers.Flatten(),
			tf.keras.layers.Dense(256, activation="relu"),
			tf.keras.layers.BatchNormalization(),
			tf.keras.layers.Dropout(0.5),
			tf.keras.layers.Dense(10, activation="softmax"),
		]
	)

	model.compile(
		optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
		loss="sparse_categorical_crossentropy",
		metrics=["accuracy"],
	)
	return model


def main():
	(ds_train, ds_test), ds_info = tfds.load(
		"svhn_cropped",
		split=["train", "test"],
		as_supervised=True,
		with_info=True,
	)

	num_train = ds_info.splits["train"].num_examples
	train_size = int(0.9 * num_train)

	ds_train = ds_train.shuffle(10_000, reshuffle_each_iteration=False)
	ds_val = ds_train.skip(train_size)
	ds_train = ds_train.take(train_size)

	batch_size = 128
	autotune = tf.data.AUTOTUNE

	ds_train = (
		ds_train.map(preprocess, num_parallel_calls=autotune)
		.cache()
		.shuffle(10_000)
		.batch(batch_size)
		.prefetch(autotune)
	)
	ds_val = (
		ds_val.map(preprocess, num_parallel_calls=autotune)
		.cache()
		.batch(batch_size)
		.prefetch(autotune)
	)
	ds_test = (
		ds_test.map(preprocess, num_parallel_calls=autotune)
		.cache()
		.batch(batch_size)
		.prefetch(autotune)
	)

	model = build_model()
	model.summary()

	callbacks = [
		tf.keras.callbacks.EarlyStopping(
			monitor="val_accuracy", patience=8, restore_best_weights=True
		),
		tf.keras.callbacks.ReduceLROnPlateau(
			monitor="val_accuracy", factor=0.5, patience=4, min_lr=1e-5
		),
	]

	model.fit(
		ds_train,
		validation_data=ds_val,
		epochs=30,
		callbacks=callbacks,
		verbose=2,
	)

	test_loss, test_accuracy = model.evaluate(ds_test, verbose=0)
	print(f"Test loss: {test_loss:.4f}")
	print(f"Test accuracy: {test_accuracy:.4f}")

	save_path = os.path.join(os.path.dirname(__file__), "svhn_model.keras")
	model.save(save_path)
	print(f"Model saved to: {save_path}")


if __name__ == "__main__":
	main()
