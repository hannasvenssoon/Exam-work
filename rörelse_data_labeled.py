import pandas as pd

df = pd.read_csv("acc_rörelse_data.csv", header = None, sep = ';')
#df.columns = ["X", "Y", "Z"]
df["label"] = "moving"

df.to_csv("acc_rörelse_labeled.csv", index = False, sep = ';', header = False)

print("Ny fil skapad")