import csv
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Operacoes_Especiais.csv', encoding='iso8859-1')
data.head()

n_op = np.zeros((3,12), dtype=np.int64)
n_op_saude = np.zeros((3,12), dtype=np.int64)
n_op_edu = np.zeros((3,12), dtype=np.int64)

for i in range(158):
    row = data.iloc[i]
    a = row['ano']
    b = row['mes']
    n_op[a-2016][b-1] +=1
    if type(row["area"]) != float:

        aux = row["area"].split(";")
        for i in range(len(aux)):
            x = aux[i]
            if x[0] == ' ': x = x[1:]
            if x[0].isupper() == False: x = x[0].upper() + x[1:]
            aux[i] = x

        #saude
        if "Saúde" in aux: n_op_saude[a-2016][b-1] +=1    
        #educação
        elif "Educação" in aux: n_op_edu[a-2016][b-1] +=1 
    

for i in range(3):
    plt.subplot(3,1,i+1)
    plt.plot(list(range(1,13)),n_op[i], color ='red')
    plt.xticks(np.arange(1,13, 1.0))
    plt.yticks(np.arange(0,15, 2.0))
    plt.grid(linestyle='-.', linewidth=1)
    y = i+2016
    plt.ylabel(str(y))
plt.xlabel('n. de operações especiais')

#saude
plt.figure(2)
for i in range(3):
    plt.subplot(3,1,i+1)
    plt.plot(list(range(1,13)),n_op_saude[i], color ='blue')
    plt.xticks(np.arange(1,13, 1.0))
    plt.yticks(np.arange(0,9, 1.0))
    plt.grid(linestyle='-.', linewidth=1)
    y = i+2016
    plt.ylabel(str(y))
plt.xlabel('n. de operações esp. area da saúde')

#edu
plt.figure(3)
for i in range(3):
    plt.subplot(3,1,i+1)
    plt.plot(list(range(1,13)),n_op_edu[i], color ='green')
    plt.xticks(np.arange(1,13, 1.0))
    plt.yticks(np.arange(0,9, 1.0))
    plt.grid(linestyle='-.', linewidth=1)
    y = i+2016
    plt.ylabel(str(y))
plt.xlabel('n. de operações esp. area educação')


plt.show()

    
