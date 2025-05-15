d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

result = {}
for k, v in d.items():
    if v >= 3:
        result[k] = v

print(result)