import csv
import pandas as pd


with open('Operacoes_Especiais.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    count = 0
    part = {'MPF':0}
    areas = {}
    ufs = {}

    #part 1
    for row in reader:
        #estatistica de parcerias
        aux = row["parceiro"].split(";")
        for x in aux:
            x = x.strip(" ")
            if x in part:
                part[x] = part[x] +1
            else:
                part[x] = 1
##            if x == "TCU":
##                print(row["nome_op"],", ",row["uf_corrigido"])
##            if  row["prej_pot"]:
##                if float(row["prej_pot"]) > 50000000:
##                    print(row["prej_pot"])

        #estatistica de areas da administração publica
        aux = row["area"].split(";")        
        for i in range(len(aux)):
            x = aux[i]
            if len(x)<2: x = 'n.c.'
            if x[0] == ' ': x = x[1:]
            if x[0].isupper() == False: x = x[0].upper() + x[1:]
            aux[i] = x
            if x in areas:
                areas[x] = areas[x] +1
            else:
                areas[x] = 1
		
        #row["area"] = ";".join(aux)        
        aux = list(row["uf_corrigido"].split(";"))
        for x in aux:
            if x[0] == ' ': x = x[1:]
            if x in ufs:
                ufs[x] = ufs[x] +1
            else:
                ufs[x] = 1
                        
            #operaçoes com parcerias:
    for i in part:
        print(i,": ",part[i])
    print("\n")

    #por areas
    for i in areas:
        print(i,": ",areas[i])
    print("\n")

	 #por ufs
    for i in ufs:
        print(i,": ",ufs[i])

