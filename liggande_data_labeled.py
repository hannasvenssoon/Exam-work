import pandas as pd

df = pd.read_csv("acc_liggande_data.csv", header = None, sep = ';')
#df.columns = ["X", "Y", "Z"]
df["label"] = "liggande"

df.to_csv("acc_liggande_labeled.csv", index = False, sep = ';', header = False)

print("Ny fil skapad")