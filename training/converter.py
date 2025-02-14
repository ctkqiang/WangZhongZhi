import tensorflow as tf

model = tf.keras.models.load_model("../assets/dog_breed_classifier.h5")

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open("dog_breed_classifier.tflite", "wb") as f:
    f.write(tflite_model)
