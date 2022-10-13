import csv
with open('gitzadacha.csv', 'r') as file:
    reader = csv.reader(file)
    file_out = open('gitzadacha2.csv', 'w')
    writer = csv.writer(file_out)
    writer.writerow(("year","region","value"))
    next(reader, None) # skip the headers
    for row in reader:
        row[0]=row[0]+'-01-01'
        writer.writerow(row)
        #print(row)
