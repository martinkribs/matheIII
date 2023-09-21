# Einlesen der .csv-Datei  Auto mit Ausgabe der ersten 10 Zeilen
import pandas as pd

file = pd.read_csv("Auto.csv", sep=";", decimal=".", nrows=100)
#print(file.head(10))

#print(file.isnull().sum())

#file.dropna(how="all",inplace=True)
#print(file.head(5))
