import csv

with open("Q2.csv", "r") as f:
    reader = csv.DictReader(f)
    data = []
    for row in reader:
        # Convert marks to integers and calculate total
        row['CPII'] = int(row['CPII'])
        row['MathsII'] = int(row['MathsII'])
        row['Chemistry'] = int(row['Chemistry'])
        row['total'] = row['CPII'] + row['MathsII'] + row['Chemistry']
        data.append(row)
    for record in data:
        print(record)
