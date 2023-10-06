import csv

filename = 'chapter_7 challenge/Chapter_7Challenge.csv'

candy_type = {}

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        candy = row[2]


























        candys = [candy.lower()]
        for candy in candys:
            if candy in candy_type.keys():
                print('{} is a duplicate candy'.format(candy))
                candy_type[candy] = candy_type[candy] + 1
            else:
                print('{} is a unique candy'.format(candy))
                candy_type[candy] = 1
    print(candy_type)
#candys.sort()
#print(candys)
