import pandas as pd

df = pd.concat(
    [
        pd.read_csv('acc_liggande_labeled.csv', sep = ';', names=["x", "y", "z", "label"]),
        pd.read_csv('acc_stående_labeled.csv', sep = ';', names=["x", "y", "z", "label"]),
        pd.read_csv('acc_rörelse_labeled.csv', sep = ';', names=["x", "y", "z", "label"]),
                    
    ], 
    ignore_index = True
)

df.to_csv('acc_full_data.csv', index = False, sep = ';', header = False)

print('Ny fil skapad')