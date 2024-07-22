# 1. Keys, Values, Items
d1 = {'Name':'Thomas', 'Age':25, 'Country':'India', 'Class':'Data Science', 'Grade':8.75}
keys = list(d1.keys())
values = list(d1.values())
items = list(d1.items())
print(keys, '\n', values, '\n', items, '\n\n')

print(f"{keys[0]}\n{values[0]}\n{items[0]} ---> {items[0][0]} and {items[0][1]}")



# 2. Update (like replace), get, clear
d2 = {'Name':'Felix', 'Country':'Portugal', 'Grade':9.15}
d1.update(d2)
print(d1, '\n')

print(d1.get('Name'), d1.get('Age'), d1.get('Grade'), d1.get('Gender'))
print(d1['Name'], d1['Age'], d1['Grade'], '\n')

print(d1.clear())



# 3. Pop (remove by key) vs popitem (remove last pair every time)
d3 = {'Name':'Thomas', 'Age':25, 'Country':'India', 'Class':'Data Science', 'Grade':8.75, 'Region':'Athens', 'YearsAtWork':5}
d3.pop('Name')
d3.pop('Country')
print(d3, '\n')

d3.popitem()
print(d3)



# 4. Copy and add pairs
d4 = {'Name':'Thomas', 'Age':25, 'Country':'India', 'Class':'Data Science', 'Grade':8.75, 'Region':'Athens', 'YearsAtWork':5}
d5 = d4.copy()

d4.popitem()
d4['Name'] = 'Sabrina'

d5['Height'] = '185 cm'
print(d4, '\n', d5)



# 5. Create a dictionary with the SAME VALUE for every key
array = ['String1', 'String2', 'String3', 'String4', 'String5']
value = 'Hello'
d6 = {key:value for key in array}
print(d6)
d7 = dict.fromkeys(array, value)
print(d7)
