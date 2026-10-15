import csv

totals = {}

with open('items.csv','r') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        if row['metal'] == 'Gold':
            weight = float(row['weight_gm'])
            totals[row['purity']]=totals.get(row['purity'],0)+weight
for key,value in totals.items():
    print(f"{key}: {value}")