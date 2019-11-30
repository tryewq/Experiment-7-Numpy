import numpy as np
X = np.random.rand(5,5)
m = X.mean()
s = X.std()
Z = (X-m)/s

np.save('X_normalized', Z)