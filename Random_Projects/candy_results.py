import csv

filename = 'chapter_7 challenge/Chapter_7Challenge.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    candys = []
    for row in reader:
        candy = row[2]
        candys.append(candy.lower())

candys.sort()
print(candys)
new_list = []
dup_list = []
for x in candys:
    if x not in new_list:
        new_list.append(x.lower())
    else:
        dup_list.append(x)


print(f"Unique items: {new_list}")
print(f"Duplicate items: {dup_list}")
