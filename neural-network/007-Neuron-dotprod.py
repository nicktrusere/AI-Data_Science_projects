import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2
# both vectors order of wieghts and input can be (weight,inputs)
output = np.dot(inputs, weights) + bias
print(output)