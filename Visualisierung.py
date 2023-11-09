import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("Dataset/Auto.csv", sep=";", decimal=",")
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
# print(file.iloc[35:40])

mw = file["displacement"].mean()
file["displacement"].fillna(mw, inplace=True)

mw = file["horsepower"].mean()
file["horsepower"].fillna(mw, inplace=True)

file.dropna(how="any", inplace=True)
print(file.isnull().sum())

# univariate Analyse
print(file.describe().round(2))
# Datentyp abfragen
print(file.dtypes)

# Histogramm
file["displacement"].plot(kind="hist", color="blue")
# Beschriftung des Histogramms
plt.title("Histogramm von Displacement")
plt.xlabel("Klassen")
plt.ylabel("Höhe")
plt.show()

# Boxplot
file[["mpg", "acceleration"]].plot(kind="box", showfliers=True)
plt.show()
