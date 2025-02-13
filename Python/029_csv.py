import csv
with open('csv_file.csv') as f:
    csv_reader = csv.reader(f,delimiter=',')
    linecount = 0
    for i in csv_reader:
        print(f'{i}')