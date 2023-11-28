import numpy as np
import tensorflow as tf

# Load the TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path="tf_lite_model.tflite")
interpreter.allocate_tensors()

# Load the Keras model
keras_model = tf.keras.models.load_model("tf_model_fashion_mnist.h5")

# Prepare test input data (replace this with your actual test data)
test_input = np.random.rand(1, 28, 28).astype(np.float32)

# Run inference with TensorFlow Lite model
interpreter.set_tensor(interpreter.get_input_details()[0]['index'], test_input)
interpreter.invoke()
tflite_model_predictions = interpreter.get_tensor(interpreter.get_output_details()[0]['index'])

# Run inference with Keras model
keras_model_predictions = keras_model.predict(test_input)

print("TensorFlow Lite Model Prediction:", tflite_model_predictions)
print("Keras Model Prediction:", keras_model_predictions)
