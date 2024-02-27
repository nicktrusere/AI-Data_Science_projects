import numpy as np

np.random.seed(0)

X = [[1, 2, 3, 2.5],                  # Training data - 3 samples
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]

class layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = np.random.randn(n_inputs, n_neurons)
    def forward(self):
        pass
print(np.random.randn(4, 3))
# To maintain values - values bigger than 1 
print(0.10*np.random.randn(4, 3))