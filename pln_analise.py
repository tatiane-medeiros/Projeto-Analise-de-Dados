import csv
import pandas as pd
import math

data = pd.read_csv('Operacoes_Especiais.csv', encoding='iso8859-1')
data.head()

municipio, org = [], []

for i in range(16):
    row = data.iloc[i]
    text = row["Release"].split()
    municipio, org = [], []
    for x in range(len(text)):
        if text[x] == "município" or text[x] == "municipal" or text[x] == "cidade":
            k=2
            name = ""
            if text[x+1] == "de" or text[x+2] == "de":
                if text[x+2] == "de": k = k+1
                while text[x+k].endswith('.')==False and text[x+k].endswith(',')==False and text[x+k] != "e":
                    name += text[x+k]+" "
                    k = k+1
                name += text[x+k][:-1]
                municipio.append(name)
            
                x = x+k
        elif text[x] == "cidades" or text[x] == "municípios":
            k=2
            name = ""
            if text[x+1] == "de" or text[x+2] == "de":
                if text[x+2] == "de": k = k+1
                while text[x+k].endswith('.')==False:
                    if text[x+k]!= "em" and text[x+k]!= "e": name += text[x+k]+" "
                    k = k+1
                name += text[x+k][:-1]
                municipio.append(name)
                
    print(municipio)
    
    
