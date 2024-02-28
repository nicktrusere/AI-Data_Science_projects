import math
import numpy as np
import nnfs

nnfs.init()

layer_outputs = [4.8, 1.21, 2.385]
# layer_outputs = [4.8, 4.79, 4.25]

# E = 2.718281828459045
E = math.e

exp_values = np.exp(layer_outputs)

norm_values = exp_values / np.sum(exp_values)


print(norm_values)             # Normalized values
print(sum(norm_values))        # Summming it up 

# SUMMARY

# Input --> Exponentiate --> Normalize --> Output ==> Softmax function