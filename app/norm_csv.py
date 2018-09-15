import csv
import datetime

class Normalize:

    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile

        with open(infile, encoding='utf-8') as infile, open(outfile, "w", encoding='utf-8') as outfile:
            reader = csv.reader(infile, delimiter=',')
            writer = csv.writer(outfile)
            headers = next(reader, None) #don't parse headers
            writer.writerow(headers) #write headers to new csv

            for row in reader:
                row[0] = datetime.datetime.strptime(row[0], "%m/%d/%y %H:%M:%S %p") + datetime.timedelta(hours=3)
                row[2] = row[2].zfill(5) #prepend with 0s until 5
                row[3] = row[3].upper()
                row[4] = Normalize.get_float(row[4])
                row[5] = Normalize.get_float(row[5])
                row[6] = row[4] + row[5]
                writer.writerow(row)

    def get_float(t):
        hr, mm, sec = map(float, t.split(':'))
        inMs = ((hr * 60 + mm) * 60 + sec) * 1000
        return int(inMs)

infile = input("Enter the file to normalize: ")
outfile = input("Enter the normalized file name: ")
Normalize(infile, outfile)
