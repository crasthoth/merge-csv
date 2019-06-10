import glob, csv, os
dirname = os.path.dirname(os.path.abspath(__file__))
interesting_files = glob.glob(os.path.join(dirname, "dump", "*.csv"))

header_saved = False
with open(os.path.join(dirname, 'output.csv'), 'w') as fout:
    writer = csv.writer(fout)
    for filename in interesting_files:
        with open(filename) as fin:
            header =  next(fin)
            if not header_saved:
                writer.writerows(header) # you may need to work here. The writerows require an iterable.
                header_saved = True
            writer.writerows(fin.readlines())
