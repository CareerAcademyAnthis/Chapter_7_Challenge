import csv
# Pull in the CSV file
filename = 'Chapter_7Challenge.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, colum_header in enumerate(header_row):
        print(index, colum_header)

    # Loop through the csv file and create two lists
    student_names = []
    candy_type_1 = []
    candy_type_2 = []
    candy_price_1 = []
    candy_price_2 = []

    for row in reader:
        stu_name = row[0]
        candy_1 = row[1]
        candy_2 = row[3]
        price_1 = float(row[2])
        price_2 = float(row[4])
        # add the code here that will append each variable above into the correct list.

        student_names.append(stu_name.lower())
        candy_type_1.append(candy_1.lower())
        candy_type_2.append(candy_2.lower())
        candy_price_1.append(price_1)
        candy_price_2.append(price_2)

# Print each list
print(student_names)
print(candy_type_1)
print(candy_price_1)
print(candy_type_2)
print(candy_price_2)

list_candy_1 = zip(candy_type_1, candy_price_1)
list_candy_2 = zip(candy_type_2, candy_price_2)

candy_1 = list(list_candy_1)
candy_2 = list(list_candy_2)

candy_survey_dict = {}
for key , value_1, value_2 in zip(student_names, candy_1, candy_2):
    candy_survey_dict[key] = [value_1, value_2]

print(candy_survey_dict)

'''
keys = [‘a‘, ’b’,]
values = [1, 2, 3]
nested_dict = {}
for key, value in zip (keys, values):
    nested_dict [key] = {‘value’: value}
    print (nested_dict) # {‘a’: {‘value’: 1}, ‘b’: {‘value’: 2}, ‘c’: {‘value’: 3}}

list_of_dicts = [{‘a’: 1}, {‘b’: 2}]
new_dict = {‘c’: 3}
list_of_dicts.append (new_dict)
print (list_of_dicts) # [{‘a’: 1}, {‘b’: 2}, {‘c’: 3}]
'''