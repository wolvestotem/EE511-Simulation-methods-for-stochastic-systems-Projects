import numpy as np

X = np.random.randn(3,1)
mu = np.array([[1],[2],[3]])
sigma = np.array([[3,-1,1],[-1,5,3],[1,3,4]])
value, vector = np.linalg.eig(sigma)
A = vector.dot(np.diag(np.sqrt(value)))
Y = A.dot(X)+mu
print(Y)