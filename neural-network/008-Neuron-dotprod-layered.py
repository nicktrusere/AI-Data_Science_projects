import numpy as np

inputs = [1, 2, 3, 2.5] # Vector

weights = [[0.2, 0.8, -0.5, 1.0],  # Matrix - 3 neurons
            [0.5, -0.91, 0.26, -0.5],
            [0.26, -0.27, 0.17, 0.87]]

biases = bias1 = [2, 3, 0.5]
# Need 3  values from neuron - indexed as output - cannot interchange (inputs, weights) - value error
output = np.dot(weights, inputs) + biases
print(output)