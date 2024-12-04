import numpy as np
import pandas as pd

#Test Romana
#Difera 4 si 9

#1
matrix_1 = np.loadtxt("matrix.txt", delimiter=' ', dtype=int)
print(matrix_1)

#2
arr2 = np.random.uniform(-10,10,size=50)
series2 = pd.Series(arr2,index=["R_"+str(i+1) for i in range(len(arr2))])
print(series2)

#3
arr3 = np.random.uniform(-10,10,size=(10,7))
df3 = pd.DataFrame(arr3, index=['R'+str(i+1) for i in range(arr3.shape[0])],
                   columns=['V'+str(i+1) for i in range(arr3.shape[1])])
print(df3)

#4

#a
arr4 = np.full(shape=(7,7),fill_value=9,dtype=float)
print(arr4)

#b
arr4[1:arr4.shape[0]-1,1:arr4.shape[1]-1] = 0
arr4[0,:] = 5
arr4[:,-1] = 5
arr4[-1,:] = 5
arr4[:,0] = 5
print(arr4)

#5
dict5 = {"Stud"+str(i+1):np.random.randint(1,11,size=5) for i in range(7)}
df5 = pd.DataFrame(dict5)
print(df5)

#6
series16 = pd.read_csv('series1.csv',header=None).iloc[:,0]
series26 = pd.read_csv('series2.csv',header=None).iloc[:,0]
dict6 = {
    'C_1':series16,
    'C_2':series26
}
df6 = pd.DataFrame(dict6)
print(df6)

#7
df7 = pd.read_csv('KO.csv')
df7['RV'] = df7.apply(lambda row: (row['Close']-row['Open'])/(row['High']-row['Low']),axis=1)
print(df7)
df7.to_csv("KO_RV.csv",index=False)

#8
dict8 = {'An_'+str(i+1):{'Stud_'+str(j+1):np.random.randint(1,11,size=3) for j in range(8)} for i in range(3)}
df8 = pd.DataFrame(dict8)
print(df8)

#9
arr9 = np.zeros((7,7))
arr9[0,:] = 4
arr9[:,-1] = 4
arr9[-1,:] = 4
arr9[:,0] = 4
np.fill_diagonal(arr9,[(33,11)[x!=3]for x in range(7)])
print(arr9)

#9 alternativa functie

def funct(i, j):
    result = np.zeros_like(i, dtype=float)

    result[i == j] = 11
    result[(i == j) & (i == 3)] = 99
    result[(i == 0) | (i == 6)] = 4
    result[(j == 0) | (j == 6)] = 4

    return result

arr9 = np.fromfunction(lambda i,j:funct(i,j),(7,7),dtype=float)
print(arr9)
