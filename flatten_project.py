def flatten_list(x):
    result = []
    for item in x:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
            
    return result

def reverse_list(x):
    result = []
    for item in reversed(x):
        if isinstance(item, list):
            result.append(reverse_list(item))
        else:
            result.append(item)
    return result


nested_list = [[1, ['araba', ['kedi']], 2], [[[3]], 'kopek'], 4, 5]
flattened_list = flatten_list(nested_list)
print("Flattened Liste:", flattened_list)

nested_list_to_reverse = [[-1, -2], [-3, -4], [-5, -6, -7]]
reversed_list = reverse_list(nested_list_to_reverse)
print("Reversed Liste:", reversed_list)