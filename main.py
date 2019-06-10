import glob
import csv
interesting_files = glob.glob("/home/tcs/PYTHONMAP/test1/*.csv")

header_saved = False
with open('/home/tcs/PYTHONMAP/output.csv', 'w') as fout:
    writer = csv.writer(fout)
    for filename in interesting_files:
        with open(filename) as fin:
            header =  next(fin)
            if not header_saved:
                writer.writerows(header) # you may need to work here. The writerows require an iterable.
                header_saved = True
            writer.writerows(fin.readlines())
