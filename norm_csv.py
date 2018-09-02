import csv
import datetime

def normalize_file(infile, outfile):
    with open(infile, encoding='utf-8') as infile, open(outfile,"w") as outfile:
        reader = csv.reader(infile)
        headers = next(reader, None) #skip the headers
        writer = csv.writer(outfile)

        for row in reader:
            timestamp = row[0]
            print(timestamp)


        if headers:
            writer.writerow(headers)


















infile = input("Enter the file to normalize: ")
outfile = input("Enter the normalized file name: ")
normalize_file(infile, outfile)
