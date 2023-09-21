# Einlesen der .csv-Datei  Auto mit Ausgabe der ersten 10 Zeilen
import pandas as pd

file = pd.read_csv("Auto.csv", sep=";", decimal=",")
print(file.head(10))

# Abfrage Datentypen der Spalten
print(file.dtypes)

print(file["mpg"].iloc[0:7])

print("Mittelwert der 1. Spalte", file["mpg"].mean().round(3))

# NAN-Behandlung
print(file.isnull().sum())

# Löschen einer Zeile nur mit NAN
file.dropna(how="any", inplace=True)

print(file.head(5))
print(file.isnull().sum())

mw = file["mpg"].mean()
print("Mittelwert:", mw)

file["mpg"].fillna(mw, inplace=True)
print(file["mpg"].iloc[30:40])
