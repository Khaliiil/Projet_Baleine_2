import numpy as np
import aifc
import csv


def readAIFF(filePath):
    f = aifc.open(filePath, 'r')
    numFrames = f.getnframes()
    print numFrames
    contentFrames = f.readframes(numFrames)
    f.close()
    return np.fromstring(contentFrames, np.short).byteswap()


def read_csv(file_path, has_header=True, limit=None):
    with open(file_path, 'rU') as f:
        dialect = csv.Sniffer().sniff(f.read(1024), ',')
        f.seek(0)
        csvReader = csv.reader(f, delimiter=',', dialect=dialect)

        header = []
        if has_header:
            header = csvReader.next()
        data = []
        for i, line in enumerate(csvReader):
            data.append(line)
            if limit == (i+1):
                break
    return header, data


def write_csv(file_path, data):
    with open(file_path, "w") as f:
        for line in data:
            f.write(",".join(line) + "\n")

