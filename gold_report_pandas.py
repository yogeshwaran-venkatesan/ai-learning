import pandas as pd
# 1. read items.csv into df
df = pd.read_csv('items.csv')
# 2. keep only Gold rows → save in a variable called gold
gold = df[df["metal" ]=='Gold']
# 3. group gold by purity, sum weight_gm → save in totals
totals = gold.groupby('purity')['weight_gm'].sum()
# 4. loop through totals and print like:  22K : 75.30 g
for purity, weight_gm in totals.items():
    print(f'{purity} : {weight_gm}g')
