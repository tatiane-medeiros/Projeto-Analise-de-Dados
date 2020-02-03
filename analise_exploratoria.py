import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
            if not x: x = 'n.c.'
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

    #plt.subplot(311)
    plt.figure(1)
    plt.bar(range(len(part)), list(part.values()), align='center')
    plt.xticks(rotation=45)
    plt.xticks(range(len(part)), list(part.keys()))
    plt.yticks(np.arange(0,161, 20.0))
   # plt.xlabel("Parcerias CGU com outras entidades")
    plt.title("Parcerias CGU com outras entidades")

    plt.figure(2)
    plt.bar(range(len(areas)), list(areas.values()), align='center', color='cyan')
    plt.xticks(rotation=90)
    plt.xticks(range(len(areas)), list(areas.keys()))
    plt.title("Áreas dos recursos envolvidos nas operações")
    
    plt.figure(3)
    plt.bar(range(len(ufs)), list(ufs.values()), align='center', color = 'red')
    plt.xticks(rotation=45)
    plt.xticks(range(len(ufs)), list(ufs.keys()))
    plt.yticks(np.arange(0,21, 2.0))
    plt.title("Quantidade de operações por estado")
    plt.show()

