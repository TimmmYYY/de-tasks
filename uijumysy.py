import csv

month = {
    "Jan": "01-01",
    "Feb": "02-01",
    "Mar": "03-01",
    "Apr": "04-01",
    "May": "05-01",
    "Jun": "06-01",
    "Jul": "07-01",
    "Aug": "08-01",
    "Sep": "09-01",
    "Oct": "10-01",
    "Nov": "11-01",
    "Dec": "12-01"

    }
#print(thisdict['Nov'])
with open('uijumysy.csv', 'r') as file:
    reader = csv.reader(file)
    file_out = open('uijumysy2.csv', 'w')
    writer = csv.writer(file_out)
    writer.writerow(("year","region","value"))
    next(reader, None)
    for row in reader:
        #print(row[0][5:8])
        print(row[0][-3:])
        #print(row[0][5:])
        print(row[0][0:4])
        print(month[row[0][-3:]])
        row[0]=row[0][0:5
        ]+month[row[0][-3:]]
        #row[0]=row[0]+'-01-01'
        writer.writerow((row))
'''
with open('uijumysy.csv', 'r') as file:

    reader = csv.reader(file)
    file_out = open('uijumysy2.csv', 'w')
    writer = csv.writer(file_out)
    writer.writerow(("year","region","value"))
    #writer = csv.writer(file)
    next(reader, None)
    for row in reader:
        if  "Feb" in row[0]  :
            s= row[0]
            row[0] = s[:4] +'-02-01'
        elif "Mar" in row[0]  :
            s= row[0]
            row[0] = s[:4] +'-03-01'
        writer.writerow((row))
        print(row)
'''
