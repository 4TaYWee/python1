'''
Here's an example of building a simple neural network for classifying handwritten digits using TensorFlow's Keras API in Python:

Python
'''
from tensorflow import keras

# Define the model
model = keras.Sequential([
keras.layers.Flatten(input_shape=(28, 28)),  # Flatten 28x28 images
keras.layers.Dense(128, activation="relu"),  # Dense layer with 128 neurons and ReLU activation
keras.layers.Dense(10, activation="softmax")  # Output layer with 10 neurons (for 10 digits) and softmax activation
])

# Compile the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Load the MNIST dataset (modify for your dataset)
(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()

# Preprocess the data (normalize pixel values)
train_images = train_images.reshape(-1, 28, 28, 1)  # Reshape for convolutional layers (if applicable)
train_images = train_images.astype("float32") / 255.0
test_images = test_images.reshape(-1, 28, 28, 1)
test_images = test_images.astype("float32") / 255.0

# Train the model
model.fit(train_images, train_labels, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Test accuracy:", test_acc)

'''
This code defines a sequential model with three layers:
Flatten: Flattens the 28x28 image data into a 1D vector.
Dense: A hidden layer with 128 neurons and ReLU activation for non-linearity.
Dense: Output layer with 10 neurons (one for each digit class) and softmax activation to generate probability distribution.
The model is then compiled with the Adam optimizer, sparse categorical crossentropy loss (for multi-class classification), and accuracy metric.
Note:
This is a basic example. You can modify the architecture (number of layers, neurons, activation functions) for more complex tasks.
This code uses the MNIST dataset for demonstration. You'll need to replace it with your dataset and adjust preprocessing accordingly.
Źródła
1. https://github.com/AIdjIO/TensorFlow-Course
'''
