import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
import time

mu1 = [0,0]
mu2 = [0,-0.5]
cov1 = [[0.5, 0], [0, 1]]
cov2 =  [[1, 0], [0, 5]]
p = 0.6
sample = 300
data = []
prelabel = []

for i in range(sample):
    if np.random.rand()<p:
        data.append(multivariate_normal.rvs(mu1,cov1))
        prelabel.append(0)
    else:
        data.append(multivariate_normal.rvs(mu2,cov2))
        prelabel.append(1)

data = np.array(data);prelabel = np.array(prelabel)
start_time = time.time()
gmm = GaussianMixture(n_components=2, covariance_type='full',random_state=1).fit(data)
end_time = time.time()
label = gmm.predict(data)
err_num = sum(prelabel!=label)
err_rate = err_num/sample
mu1_=gmm.means_[0]
mu2_=gmm.means_[1]

print('accuracy',1-err_rate)
print(end_time-start_time)
print(gmm.means_,'\n',gmm.covariances_)
print(gmm.weights_)
