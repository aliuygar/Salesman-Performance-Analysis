import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

with open("C:/Users/Uygar/Documents/salesman-performance-analysis/Sales.csv", "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)

    with open("sales.csv", "w+", encoding="utf-8") as sales:

        wtr = csv.writer(sales)
        for i in csv_reader:

            wtr.writerow((i[1], i[2], i[3], i[4]))



with open ("sales.csv","r",encoding="utf-8") as sales:

    read=csv.reader(sales)
    new = list()
    textbox_name = input("Name  :")
    control=0
    for i in read:
        if len(i)==4 and i[3]==textbox_name :
            control+=1
            print(i)
            new.append(i)
    if control==0:
        print("NO SALES INynuuns NAME")
    else:

        file_name = textbox_name + ".csv"

        with open(file_name, "w+", encoding="utf-8", newline='') as file2:
            csvv = csv.writer(file2)

            for i in new:
                csvv.writerow((i[0], i[1], i[2], i[3]))