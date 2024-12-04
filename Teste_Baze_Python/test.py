import numpy as np
import pandas as pd


#Rezervare Liste
#1

def func(i,j):
    if i==j:
        if i==3 :
            return 77
        else:
            return 33

    if i==0 or i==6:
        return 7

    if j==0 or j==6:
        return 7

    return 0
arr1 = np.array([[np.float64(func(i,j)) for j in range (7)] for i in range(7)])

print(arr1)

arr2 = np.array([[np.nan for j in range(7)] for i in range(7)])
print(arr2)

arr2[1:6,1:6] = 0
arr2[0,0:7] = 5
arr2[0:7,0] = 5
arr2[6,0:7] = 5
arr2[0:7,6] = 5

print(arr2)

#3
arr3 = np.array([[arr2[i,j] for j in range(1,6)] for i in range(1,6)])

print(arr3)

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