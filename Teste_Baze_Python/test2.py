import numpy as np
import pandas as pd

#Difera 1,2,3

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
arr4 = np.zeros(shape=(7,7))
arr4[0:arr4.shape[0],0:arr4.shape[1]] = 9
print(arr4)

#b
arr4[1:arr4.shape[0]-1,1:arr4.shape[1]-1] = 0
arr4[0,0:arr4.shape[1]] = 5
arr4[arr4.shape[1]-1,0:arr4.shape[1]] = 5
arr4[0:arr4.shape[0],0] = 5
arr4[0:arr4.shape[0],arr4.shape[1]-1] = 5
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
def funct(i,j):
    if i==j:
        if i==3:
            return 99
        else:
            return 11
    if i==0 or i==6:
        return 4
    if j==0 or j==6:
        return 4
    return 0

arr9 = np.array([[np.float64(funct(i,j)) for j in range(7)] for i in range(7)] )
print(arr9)

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