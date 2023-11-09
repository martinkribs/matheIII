import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

file = pd.read_csv("Datasets/Auto.csv", sep=";", decimal=",")

# Berechnung der Korrelation
print(file.corr().round(2))

# Visualisierung der Korrelationsmatrix
corr = sns.heatmap(file.corr(), mask=np.triu(file.corr(), k=1))
plt.show()
