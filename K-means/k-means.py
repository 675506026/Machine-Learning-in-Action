from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets._samples_generator import make_blobs
from sklearn import metrics

def draw(m_kmeans,X,y_pred,n_clusters):
    centers = m_kmeans.cluster_centers_
    print(centers)
    plt.scatter(X[:, 0], X[:, 1], c=y_pred, s=50, cmap='viridis')
    #中心点（质心）用红色标出
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)
    print("Calinski-Harabasz score：%lf"%metrics.calinski_harabasz_score(X, y_pred) )
    plt.title("K-Means (clusters = %d)"%n_clusters,fontsize=20)
    plt.show()

X, y_true = make_blobs(n_samples=300, centers=4,cluster_std=0.60)

m_kmeans = KMeans(n_clusters=4)
m_kmeans.fit(X)
y_pred = m_kmeans.predict(X)
draw(m_kmeans,X,y_pred,4)