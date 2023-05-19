# comprehension for list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:  # в виде цикла
  if "a" in x:
    newlist.append(x)

newlist = [x for x in fruits if "a" in x]  # в виде comprehension
newlist2 = [x if x != "banana" else "orange" for x in fruits]  # в виде comprehension

print(newlist)
print(newlist2)


# comprehension for dict
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_original_dict = {}
for k, v in original_dict.items():  # в виде цикла
    if v % 2 == 0:
        new_original_dict[k] = v
print(new_original_dict)

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}  # comprehension для словаря
print(even_dict)


# comprehension for set
vlans = [10, '30', 30, 10, '56']
unique_vlans1 = set()
for vlan in vlans:  # в виде цикла
    unique_vlans1.add(int(vlan))
print(unique_vlans1)

unique_vlans = {int(vlan) for vlan in vlans}  # в виде comprehension

print(unique_vlans)