from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        read_file = csv.DictReader(file, delimiter=",", quotechar='"')
        content = []
        for row in read_file:
            content.append(row)
    return content
