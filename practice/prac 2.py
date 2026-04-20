def analyze_dict_keys(d):
    symbols = set()
    for key in d.keys():
        if type(key) != str:
            continue
        has_digit = False
        for ch in key:
            if ch.isdigit():
                has_digit = True
                break
        if has_digit:
            continue
        for ch in key:
            if ch != ' ' and ch not in '.,!?;:-_()[]{}':
                symbols.add(ch)
    return symbols
punctuation = '.,!?;:-_()[]{}'
d = {
    'hello': 1,
    'world123': 2,
    'hello world': 3,
    'python!': 4,
    'test-key': 5,
    'data': 6,
    123: 7,
    'abc': 8,
    'a!bc#': 9
}
result = analyze_dict_keys(d)
print(sorted(result))

# #37
# factorial = lambda d: {k: factorial(v) if v < 6 else v for k, v in d.items()}
# data = {"a": 3, "b": 5, "c": 7, "d": 4}
# print(factorial(data))

def top_k_smallest_unique(nums, k):
    unique = set(nums)
    sorted_nums = sorted(unique)
    result = set()
    for i in range(min(k, len(sorted_nums))):
        result.add(sorted_nums[i])
    return result
nums = [5, 2, 8, 2, 3]
print(top_k_smallest_unique(nums, 2))