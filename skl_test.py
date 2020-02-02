import matplotlib.pyplot as plt

from sklearn.datasets import make_classification

plt.figure(figsize=(8, 6))
plt.subplots_adjust(bottom=.05, top=.9, left=.05, right=.95)

plt.subplot(221)
plt.title("One informative feature, one cluster", fontsize='small')
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1)

plt.subplot(222)
plt.title("Two informative features, one cluster", fontsize='small')
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=2, n_clusters_per_class=1)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1)

plt.subplot(223)
plt.title("Two informative features, two clusters", fontsize='small')
X2, Y2 = make_classification(n_features=2, n_redundant=0, n_informative=2)
plt.scatter(X2[:, 0], X2[:, 1], marker='o', c=Y2)


plt.subplot(224)
plt.title("Multi-class, two informative features, one cluster", fontsize='small')
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=2, n_clusters_per_class=1, n_classes=3)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1)

plt.show()
