import pandas as pd

file = pd.read_csv("Datasets/Auto.csv", sep=";", decimal=",")
print(file.head(10))

# Abfrage Datentypen der Spalten
print(file.dtypes)

# Beschränkung auf Zeile und Spalte
print(file["mpg"].iloc[0:7])

print("Mittelwert der 1. Spalte: ", file["mpg"].mean().round(3))

# NAN-Behandlung
print(file.isnull().sum())

# Löschen einer Zeile nur mit NAN
file.dropna(how="all", inplace=True)
print()
print(file.head(5))
print(file.isnull().sum())

mw = file["mpg"].mean()
print("Mittelwert: ", mw)

file["mpg"].fillna(mw, inplace=True)
print(file.iloc[35:40])
