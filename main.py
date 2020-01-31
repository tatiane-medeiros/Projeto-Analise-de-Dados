import csv

with open('Operacoes_Especiais.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    count = 0
    part = {'MPF':0}
    
    for row in reader:
        aux = row["parceiro"].split(";")
        for x in aux:
            if x in part:
                part[x] = part[x] +1
            else:
                part[x] = 1

#print(count)

#operaçoes com parcerias:
for i in part:
    print(i,": ",part[i])
