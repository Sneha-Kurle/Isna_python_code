capitals={'USA':'Washington', 'india': 'New Delhi', 'Germony':'Berlin'}
print(capitals)
keys=capitals.keys()
value=capitals.values()
items=capitals.items()
for keys, value in items:
    print(f'{keys}: {value}')