import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans

data = np.loadtxt(open("faithful.dat.txt",'rb'),skiprows=26)
data = data[:,1:3]
kmeans = KMeans(n_clusters=2, random_state=1).fit(data)
label = kmeans.predict(data)
centers = kmeans.cluster_centers_
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.scatter(data[:,0],data[:,1],c=label,s=40)
ax1.scatter(centers[:,0],centers[:,1],c='red',s=80)
ax1.set_title("Kmeans Clusters",fontsize=15)
ax1.set_xlabel("eruptions")
ax1.set_ylabel("waiting")
plt.show()

gmm = GaussianMixture(n_components=2,covariance_type='full',random_state=1).fit(data)
labelgm = gmm.predict(data)
mu = gmm.means_
covariance = gmm.covariances_
t = gmm.weights_
x,y = np.mgrid[1:5.5:0.01,40:100:0.1]
pos = np.empty(x.shape+(2,))
pos[:,:,0] = x; pos[:,:,1] = y
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.contourf(x,y,t[0]*multivariate_normal.pdf(pos,mu[0,:],covariance[0,:,:])+t[1]*multivariate_normal.pdf(pos,mu[1,:],covariance[1,:,:]))
ax2.scatter(data[:,0],data[:,1],c=labelgm,s=20,cmap='winter')
ax2.set_title("Gaussian mixture",fontsize=15)
ax2.set_xlabel("eruptions")
ax2.set_ylabel("waiting")
plt.show()
