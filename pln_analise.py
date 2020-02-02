import csv
import pandas as pd
import math
from nltk.corpus import stopwords
#from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

data = pd.read_csv('Operacoes_Especiais.csv', encoding='iso8859-1')
data.head()

municipio, org = [], []
#stopwords.words('portuguese')

cidlist = ["município","municipal", "cidade"]
cidlist2 = ["cidades", "municípios"]
uflist = ['AC','AL','AP', 'AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']

for i in range(16):
    row = data.iloc[i]
    text = row["Release"].split()
    municipio, org = [], []
    for x in range(len(text)):
        #if text[x] == "município" or text[x] == "municipal" or text[x] == "cidade":
        if text[x] in cidlist:
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
        #elif text[x] == "cidades" or text[x] == "municípios":
        elif text[x] in cidlist2:
            k=2
            name = ""
            if text[x+1] == "de" or text[x+2] == "de":
                if text[x+2] == "de": k = k+1
                while text[x+k].endswith('.')==False:
                    if text[x+k]!= "em" and text[x+k]!= "e": name += text[x+k]+" "
                    k = k+1
                name += text[x+k][:-1]
                municipio.append(name)
    if municipio: municipio = municipio[0].split(", ")            
    print(municipio)
    
    
