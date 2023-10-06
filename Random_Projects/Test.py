keys = ['a', 'b', 'c']
other_keys = ['x', 'y', 'z']
values = [(1, 2),(3, 4)]
other_values = [4, 5, 6]



nest_dict = {}
for key, value, other_key in zip(keys, values, other_keys):
    nest_dict[key] = [value, other_key]

    print(other_keys)


print(nest_dict)



"""for x, y in nest_dict.items():
    print(f"Category: {x}")
    print(f'Items:')
    for i in y:
        print(f" {i}")
    print()"""

