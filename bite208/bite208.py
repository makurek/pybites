def find_number_pairs(numbers, N=10):
    result = []
    for i in numbers:
        number_to_find = round(N - i, 2)
        if number_to_find in list(set(numbers) - set([i])):
            result.append((i, number_to_find))
    r = []
    for p in result:
        a,b = p
        temp = (a,b) if a < b else (b,a)
        r.append(temp)
    return list(set(r))

print(find_number_pairs([0.24, 0.36, 0.04, 0.06, 0.33, 0.08, 0.20, 0.27, 0.3, 0.31,
          0.76, 0.05, 0.08, 0.08, 0.67, 0.09, 0.66, 0.79, 0.95], 1))
