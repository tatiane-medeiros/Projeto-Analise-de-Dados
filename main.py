import csv
import pandas as pd

with open('Operacoes_Especiais.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    count = 0
    part = {'MPF':0}
    areas = {}
    saude_op = []
    cod = []
    prej = []
    
    for row in reader:
        aux = row["parceiro"].split(";")
        for x in aux:
            x = x.strip(" ")
            if x in part:
                part[x] = part[x] +1
            else:
                part[x] = 1
          #  if x == "TCU":
          #      print(row["nome_op"],", ",row["uf_corrigido"])
          #  if  row["prej_pot"]:
          #      if float(row["prej_pot"]) > 50000000:
          #          print(row["prej_pot"])
          
        aux = row["area"].split(";")
        for x in aux:
            if len(x)<2: x = 'Diversos'
            if x[0] == ' ': x = x[1:]
            if x[0].isupper() == False: x = x[0].upper() + x[1:]
            if x in areas:
                areas[x] = areas[x] +1
            else:
                areas[x] = 1
            if x == 'Saúde':
                saude_op.append(row["nome_op"])
                cod.append(row["ordem_ano"]+"-"+row["ano"])
                value = 0
                if row["prej_pot"]: value = float(row["prej_pot"])
                prej.append(value)
  
#operaçoes com parcerias:
for i in part:
    print(i,": ",part[i])
print("\n")

#por areas
for i in areas:
    print(i,": ",areas[i])
print("\n")

#operacoes area da saude
df = pd.DataFrame({'nome': saude_op, 'codigo': cod, 'prejuizo':prej})


