import pandas as pd
import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist
import re

data = pd.read_csv('Operacoes_Especiais.csv', encoding='iso8859-1')
data.head()

municipio, org = [], []
#stopwords.words('portuguese')

munlist = ["município","municipal", "cidade", "prefeitura"]
munlist2 = ["cidades", "municípios"]
estlist = ["estadual", "governador", "estado"]
fedlist = ["federal", "nacional"]

#uflist = ['AC','AL','AP', 'AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']

new_nome = data['nome_op'].values
new_area = data['area'].values
new_mun = []
new_org = []

for i in range(161):
    row = data.iloc[i]
    municipio, org = [], []
    m,es,f = 0,0,0
    if type(row["Release"]) != float:
        text = row["Release"].split()
      
        for x in range(len(text)):
            if text[x] in munlist:
                m = True
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
                    
            elif text[x] in munlist2:
                m = True
                k=2
                name = ""
                if text[x+1] == "de" or text[x+2] == "de":
                    if text[x+2] == "de": k = k+1
                    while text[x+k].endswith('.')==False:
                        if text[x+k]!= "em": name += text[x+k]+" "
                        k = k+1
                    name += text[x+k][:-1]
                    municipio.append(name)

            if text[x] in estlist:
                es = True
            if text[x] in fedlist:
                f = True
                    
    if municipio: municipio = re.split('; |, | e ',municipio[0])           
    #print(municipio)
    aux = ""
    aux = ";".join(municipio)
    new_mun.append(aux)
    if m: org.append('municipal')
    if es: org.append('estadual')
    if f: org.append('federal')
    #print(org)
    aux = ""
    aux = ";".join(org)
    new_org.append(aux)

freq = FreqDist(new_org)
print(freq)

new_df = pd.DataFrame({'nome': new_nome, 'area': new_area, 'org': new_org, 'municipio': new_mun})

export_csv = new_df.to_csv (r'novo.csv', index = None, header=True) 
    
    
