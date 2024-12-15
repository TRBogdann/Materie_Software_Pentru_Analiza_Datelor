import numpy as np
import pandas as pd
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity

df = pd.read_csv("./dataIN/MortalityEU.csv")

#0. Data cleaning => Stergem Coloanele Numerice => Inlocuim datele lipsa cu None(Null)
# => Stergem Randurile cu date lipsa => Convertim randurile nenumerice la float

efa_df = (df.drop(columns=["Country"])
          .replace(":",None)
          .dropna()
          .astype(float))


#I. Verificam daca se poate realiza analiza pe factori

chi_square_value, p_value = calculate_bartlett_sphericity(efa_df)

# Test Bartlett: H0:Nu exista factoriabilitate, H1:exista factoriabilitate
# Pt un grad de incredere de 95% => comparam p-value cu 0.05 (1-0.95)
# Daca p-value < 0.05 => Respingem H0 si Acceptam H1 => Putem realiza analiza pe factori pentru setul curent de date

print("Chi-Square: "+str(chi_square_value))
print("P-Value: "+str(p_value))

#Test KMO - arata gradul de factoriabilitate, indicele trebuie sa fie > 0.5

kmo_all, kmo_model = calculate_kmo(efa_df)
print("Indice KMO "+str(kmo_model))

#II. Realizam o prima analiza factoriala pentru determinarea numarului de factori seminficativi

fa = FactorAnalyzer(n_factors=efa_df.shape[1],rotation=None)
fa.fit(efa_df)

#Test 1 pentru determinarea numarului de factor: Criteriul lui Kaiser
#Numarul de factori seminificative este numarul de valori proprii mai mari ca 0
#Factori semnificativi criteriu Kaiser => 5
eigenvalues,eigenvectors = fa.get_eigenvalues()
significant = len([x for x in eigenvalues if x>=1])
print("Number of Significant Factors: "+ str(significant))

#Test 2 pentru determinarea numarului de factori: Grafic - Regula Cotului
#Factori semnificativi regula cotului => 3

plt.scatter(range(1,efa_df.shape[1]+1),eigenvalues)
plt.plot(range(1,efa_df.shape[1]+1),eigenvalues)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

#III. Analiza Completa

fa = FactorAnalyzer(n_factors=significant,rotation="varimax")
fa.fit(efa_df)

#III.a) Influenta Factorilor Asupra Atributelor
corr_df = pd.DataFrame(fa.loadings_
                       ,index=efa_df.columns
                       ,columns=['F'+str(i+1) for i in range(significant)])

sns.heatmap(corr_df,annot=True,cmap="coolwarm")
plt.show()

#III.b)Varinta explicata de factori - ultimul element reprezinta varianta cumulativa
#(in acest caz factorii explica 70% din varianta setului de date)
print(fa.get_factor_variance())

