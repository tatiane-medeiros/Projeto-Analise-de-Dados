import csv
import pandas as pd
import math

data = pd.read_csv('Operacoes_Especiais.csv', encoding='iso8859-1')
data.head()
##data.iat[4,4]
##data.iloc[0]

##for i in range(161):
##    if data.iloc[i]["uf_corrigido"] == "PB":
##        print(data.iloc[i]["nome_op"])
        
        #part 2
saude_op,saude_cod, saude_prej =  [],[],[]
edu_op, edu_cod, edu_prej =  [],[],[]

for i in range(161):
    row = data.iloc[i]
    if type(row["area"]) == float:
        row["area"]="n.c."
    aux = row["area"].split(";")
    for i in range(len(aux)):
        x = aux[i]
        if x[0] == ' ': x = x[1:]
        if x[0].isupper() == False: x = x[0].upper() + x[1:]
        aux[i] = x
    #operacoes area da saude
    if "Saúde" in aux:        
        saude_op.append(row["nome_op"])
        saude_cod.append(str(row["ordem_ano"])+"-"+str(row["ano"]))
        value = 0
        if row["prej_pot"]: value = float(row["prej_pot"])
        saude_prej.append(value)
        
    #operacoes area da educaçao
    if "Educação" in aux:
        edu_op.append(row["nome_op"])
        edu_cod.append(str(row["ordem_ano"])+"-"+str(row["ano"]))
        value = 0
        if row["prej_pot"]: value = float(row["prej_pot"])
        edu_prej.append(value)

#operacoes area da saude
saude_df = pd.DataFrame({'nome': saude_op, 'codigo': saude_cod, 'prejuizo':saude_prej})
print(saude_df.nlargest(10, 'prejuizo'))

#operacoes area da educacao
edu_df = pd.DataFrame({'nome': edu_op, 'codigo': edu_cod, 'prejuizo':edu_prej})
print(edu_df.nlargest(10, 'prejuizo'))

        
