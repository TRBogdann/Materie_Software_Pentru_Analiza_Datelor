import numpy as np
import pandas as pd

#Difera 1,2,3

#1
arr1 = np.zeros((7,7))
arr1[0,:] = 7
arr1[-1,:] = 7
arr1[:,0] = 7
arr1[:,-1] = 7
np.fill_diagonal(arr1,[(33,77)[x==3] for x in range(7)])
print(arr1)

#alternativa funtie
def funct(i,j):
    result = np.zeros_like(i,dtype=float)

    result[(i == j)] = 33
    result[(i == j) & (j == 3)] = 77
    result[(i == 0) | (i == 6)] = 7
    result[(j == 0) | (j == 6)] = 7

    return result

arr1 = np.fromfunction(lambda  i,j:funct(i,j), (7,7), dtype=float)

#2

#a
arr2 = np.full(shape=(7,7),fill_value=np.nan,dtype=float)
print(arr2)

#b
arr2[1:arr2.shape[0]-1,1:arr2.shape[1]-1] = 0
arr2[0,:] = 5
arr2[-1,:] = 5
arr2[:,0] = 5
arr2[:,-1] = 5
print(arr2)

#3
arr3 = arr2[1:arr2.shape[0]-1,1:arr2.shape[1]-1]
print(arr3)

#4
#4
vec_4 = [np.random.uniform(0,10) for i in range(100)]
print(vec_4)
df_4 = pd.Series(vec_4,index=['L_'+str(i) for i in range(100)])
print(df_4)

#5
arr5 = np.random.uniform(0,10,(11,7))
print(arr5)
df5 = pd.DataFrame(arr5,columns=['C_'+str(i) for i in range(arr5.shape[1])],index=['L_'+str(i) for i in range(arr5.shape[0])])
print(df5)

#6
dict6 = {'S_'+str(i+1):np.random.randint(1,11,size=7) for i in range(8)}
print(dict6)

#7
stud7 = {'S_'+str(i+1):pd.Series(np.random.randint(1,11,size=5),index=['Ex_'+str(j) for j in range(5)]) for i in range(8)}
df7 = pd.DataFrame(stud7)
print(df7)

#8
series18 = pd.read_csv('series1.csv',header=None).iloc[:, 0]
series28 = pd.read_csv('series2.csv',header=None).iloc[:, 0]
print(type(series28))
dict8 ={
    'C1':series18,
    'C2':series28
}

df8 = pd.DataFrame(dict8)
print(df8)

#9
dict9 = {"An"+str(i):{'Stud'+str(j):np.random.randint(1,11,size=5) for j in range(8)} for i in range(5)}
print(dict9)
df9 = pd.DataFrame(dict9)
print(df9)