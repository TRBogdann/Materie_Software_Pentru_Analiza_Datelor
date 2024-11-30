import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("./dataIN/Teritorial.csv")

# renuntam la coloanele non numerice
test_df = df.drop(columns=["Judet", "Regiune"])

# Centram datele in jurul originii
mean = test_df.mean()
test_df = test_df - mean

#distanta se poate contruii cu matricea de covariatie
# formula covariatie: C = (X.T*X)/(n-1)

cov= np.cov(test_df.to_numpy().T)

#determinare valori propri - vezi cursurile de algebra :))
# Determinare valori propri: det(cov-lambda*Im) = 0
# lambda - valoare prorie, cov - matrice covariatie, Im - matrice identitate m linii m coloane
# Determinare vectori propri det(cov-lambda*Im)vec = 0
# vec - vector propriu , lambda a fost deja aflat
eigenvalues, eigenvectors = np.linalg.eig(cov)

# Sortare valori propri si vectori

sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues_sorted = eigenvalues[sorted_indices]
eigenvectors_sorted = eigenvectors[:, sorted_indices]

col = ['PC'+str(i+1) for i in range(len(eigenvectors_sorted))]

pc_df = pd.DataFrame(eigenvectors_sorted)
pc_df.columns = col

print(pc_df)

#valorile propri reprezinta variatia
#aflam contributia componentelor ca ponderea valorilor proprii in suma acestora

ponderi = eigenvalues_sorted / np.sum(eigenvalues)

for it in ponderi:
    print(it)

plt.bar(pc_df.columns, ponderi, color ='blue')

plt.xlabel("Componenta")
plt.ylabel("Pondere")
plt.title("Analiza componente principale")
plt.show()

#pc1 pc2 reprezinta 97% din varianta.
#putem sa le folosim pentru a vizualiza datele
#date proiectate. Formula X_proiectat = X * p
#p matrice componente ales (in cazul asta pc1,pc2)


X_pca = pd.DataFrame(test_df.dot(pc_df[["PC1",'PC2']].to_numpy()))
X_pca.columns = ["PC1","PC2"]

plt.scatter(X_pca["PC1"], X_pca["PC2"])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Projection onto the First Two Principal Components')
plt.show()

#extra
#plot componente ce contribuie cel mai mult la pc1
plt.scatter(test_df[test_df.columns[0]], test_df[test_df.columns[12]])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Projection onto the First Two Principal Components')
plt.show()

#proiectie doar pepc1
X_pc1 = pd.DataFrame(test_df.dot(pc_df[["PC1"]].to_numpy()))
X_pc1.columns = ["PC1"]
plt.scatter(X_pc1, [0 for x in range(X_pc1.shape[0])])
plt.xlabel('Principal Component 1')
plt.title('PCA Projection onto the First Principal Components')
plt.show()
