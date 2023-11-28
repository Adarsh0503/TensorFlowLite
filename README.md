# TensorFlowLite
This reop contains tensorflow model


# TensorFlow Fashion MNIST Model

## Overview
This repository contains code for training a neural network on the Fashion MNIST dataset using TensorFlow and converting it to TensorFlow Lite for deployment on edge devices.

## Contents
- `train_model.py`: Python script for training the neural network.
- `test_model.py`: Python script for testing the trained models (Keras and TensorFlow Lite) on new data.
- `tf_model_fashion_mnist.h5`: Saved Keras model file.
- `tf_lite_model.tflite`: TensorFlow Lite model file.

## How to Use
1. **Training the Model:**
   - Run `train_model.py` to train the neural network on the Fashion MNIST dataset.
   - The trained Keras model will be saved as `tf_model_fashion_mnist.h5`.
   - The TensorFlow Lite model will be saved as `tf_lite_model.tflite`.

2. **Testing the Model:**
   - Run `test_model.py` to test the trained models on new data.
   - The script will print predictions from both the TensorFlow Lite and Keras models.

3. **Dependencies:**
   - Make sure you have the necessary dependencies installed:
     ```bash
     pip install tensorflow numpy matplotlib
     ```

4. **Folder Structure:**
.
├── train_model.py
├── test_model.py
├── tf_model_fashion_mnist.h5
└── tf_lite_model.tflite



## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- Fashion MNIST dataset: [GitHub](https://github.com/zalandoresearch/fashion-mnist)

