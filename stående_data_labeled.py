import pandas as pd

df = pd.read_csv("acc_stående_data.csv", header = None, sep = ';')
#df.columns = ["X", "Y", "Z"]
df["label"] = "standing"

df.to_csv("acc_stående_labeled.csv", index = False, sep = ';', header = False)

print("Ny fil skapad")