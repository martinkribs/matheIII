import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("Datasets/Auto.csv", sep=";", decimal=",")

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
