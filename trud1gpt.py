'''
User
in python write code that Use the TensorFlow library to build a neural network.
ChatGPT
Sure, here's a simple example of how to use TensorFlow to build a neural network for image classification:

```python
'''
import tensorflow as tf
from tensorflow.keras import layers, models

# Load the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the neural network model
model = models.Sequential([
layers.Flatten(input_shape=(28, 28)),  # Flatten the input image
layers.Dense(128, activation='relu'),  # Hidden layer with 128 neurons
layers.Dropout(0.2),                    # Dropout layer to prevent overfitting
layers.Dense(10, activation='softmax')  # Output layer with 10 neurons for 10 classes
])

# Compile the model
model.compile(optimizer='adam',
loss='sparse_categorical_crossentropy',
metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test accuracy:", test_acc)


#This code uses TensorFlow's Keras API to build a simple neural network with one hidden layer for classifying handwritten digits from the MNIST dataset. The input images are 28x28 pixels, so the first layer flattens them into a 1D array. The model then has a dense hidden layer with 128 neurons, followed by a dropout layer to prevent overfitting, and finally an output layer with 10 neurons, each representing one digit. After compiling the model with an optimizer and loss function, it is trained on the training data and evaluated on the test data.
