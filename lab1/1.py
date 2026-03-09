#1 esep
def analyze_text(text):
    text_lower=text.lower()
    vowels = set("aeiouаеёиоуыэюя")
    unique_vowels = set()
    word_seen = set()
    result_words = []
    word=""
    for char in text_lower + " ":
        if char.isalpha():
            word+=char
        else:
            if len(word)>=5:
                if word[0]==word[-1] and word is not word_seen:
                    result_words.append(word)
                    word_seen.add(word)
            for ch in word:
                if ch in vowels:
                    unique_vowels.add(ch)
            word=""
    return len(unique_vowels)," ".join(result_words)
print(analyze_text("Madam, in Eden, I'm Adam."))

#2 esep
process=lambda text:" ".join([
    word[::-1]
    for word in text.split()
    if not any(character.isdigit() for character in word) and len(word)%2==0
])
text="hello 123 world test2 python code"
result=process(text)
print(result)

#3 esep
def top_k_words(text, k):
    import string
    text=text.lower()
    for punct in string.punctuation:
        text = text.replace(punct, "")
    words = text.split()
    freq = {}
    for word in words:
        sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        return [word for word, _ in sorted_items[:k]]
text = "hello world hello python world world"
print(top_k_words(text, 2))

#4 esep
filter_words = lambda text: ' '.join(
    word.lower()
    for word in text.split()
    if len([c for c in word if c.isupper()]) == 1
    and any(word[i].isupper() and i != 0 and i != len(word)-1 for i in range(len(word)))
)
text = "Menin atYm John Men BIlmEin sEN"
result = filter_words(text)
print(result)

#5 esep
def compress_text(text):
    if not text:
        return ""
    result=[]
    current_char=text[0]
    count=1
    for i in range(1,len(text)):
        if text[i].lower()==current_char.lower():
            count+=1
        else:
            if count==1:
                result.append(current_char)
            else:
                result.append(current_char+str(count))
            current_char = text[i]
            count=1
    if count==1:
        result.append(current_char)
    else:
        result.append(current_char+str(count))
    return "".join(result)
print(compress_text("aaBBcDDD"))

#6 esep
filter_words = lambda text: [word for word in text.split()
                            if len(word) >= 4
                            and len(set(word)) == len(word)
                            and word.isalpha()]
print(filter_words("hello world abc test123 book table apple tree car python code"))

#7 esep
def palindrome_words(text):
    clean_text = ""
    for char in text:
        if char.isalpha() or char.isspace():
            clean_text += char
    words = clean_text.split()
    palindromes = set()
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3 and word_lower == word_lower[::-1]:
            palindromes.add(word_lower)
    result = sorted(palindromes, key=lambda x: (-len(x), x))
    return result
text = "Анна! Нам? казак, дед... Шалаш, АННа, наМ, 123"
print(palindrome_words(text))

#8 esep
vowel_consonant = lambda text: ' '.join(
    'VOWEL' if word[0].lower() in 'aeiou' and not any(c.isdigit() for c in word)
    else 'CONSONANT' if word[0].isalpha() and not any(c.isdigit() for c in word)
    else word
    for word in text.split()
)
text = "apple car 123tree house"
print(vowel_consonant(text))

#9 esep
def alternate_case_blocks(text, n):
    text = text.replace(" ", "")
    result = ""

    for i in range(0, len(text), n):
        block = text[i:i + n]
        if (i // n) % 2 == 0:
            result += block.upper()
        else:
            result += block.lower()

    return result
print(alternate_case_blocks("HelloWorldPython", 3))

#10 esep
count_digit_words = lambda text: sum(
    1 for word in text.split()
    if any(c.isdigit() for c in word)
    and not word[0].isdigit()
    and len(word) >= 5
)

text = "hello abc123 world test1234 123abc python3"
print(count_digit_words(text))

#11 esep
def common_unique_chars(s1, s2):
    s2_chars = set()
    for char in s2:
        s2_chars.add(char)
    result = ""
    seen = set()

    for char in s1:
        if char.isalpha():
            if char in s2_chars and char not in seen:
                result += char
                seen.add(char)

    return result
s1 = "hello world 123"
s2 = "world hello 456"
print(common_unique_chars(s1, s2))

#12 esep
filter_words = lambda text: list(
    filter(
        lambda word: len(word) > 3
                     and word[0].lower() == word[-1].lower()
                     and word.lower() != word.lower()[::-1],
        text.split()
    )
)
text = "hello world level test ada rotor python noon"
result = filter_words(text)
print(result)

#13 esep
def replace_every_nth(text, n, char):
    words = text.split()
    short_word_indices = set()
    current_pos = 0

    for word in words:
        word_len = len(word)
        if word_len < 3:
            for i in range(current_pos, current_pos + word_len):
                short_word_indices.add(i)
        current_pos += word_len + 1
    result = ""
    for i, ch in enumerate(text):
        if (i + 1) % n == 0:
            if ch == ' ':
                result += ch
            elif ch.isdigit():
                result += ch
            elif i in short_word_indices:
                result += ch
            else:
                result += char
        else:
            result += ch

    return result


text = "hello world python code"
print(replace_every_nth(text, 2, '*'))

#14 esep
VOWELS = "аәеёиоөуұыіэюяaeiou"
filter_words = lambda text: ','.join(
    word for word in text.split()
    if len(set(word.lower())) > 3
    and not any(
        word.lower().count(v) > 1 for v in VOWELS
    )
)
text = "hello world python book tree house программа"
result = filter_words(text)
print(result)

#15 esep
def word_pattern_sort(text):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    clean_text = text
    for p in punctuation:
        clean_text = clean_text.replace(p, ' ')

    words = clean_text.split()
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)

    def count_vowels(word):
        return sum(1 for c in word.lower() if c in 'aeiou')

    result = []
    for length in sorted(groups.keys()):
        sorted_group = sorted(groups[length],
                              key=lambda w: (-count_vowels(w), w))
        result.extend(sorted_group)

    return result


text = "hello world python code apple"
print(word_pattern_sort(text))

#16 esep
def transform_list(nums):
    result = []

    for num in nums:
        if num < 0:
            continue
        if num % 2 == 0:
            result.append(num ** 2)
        elif num > 10 and num % 2 != 0:
            digit_sum = 0
            n = num
            while n > 0:
                digit_sum += n % 10
                n //= 10
            result.append(digit_sum)
        else:
            result.append(num)

    return result


nums = [-5, 4, 13, 7, 20, 11, 2]
print(transform_list(nums))

#17 esep
process_numbers = lambda nums: list(
    map(
        lambda x: x ** 2,
        filter(
            lambda x: (x % 3 == 0 or x % 5 == 0)
                      and x % 15 != 0
                      and len(str(abs(x))) % 2 == 1,
            nums
        )
    )
)
numbers = [3, 5, 9, 10, 15, 25, 30, 33, 45, 50, 100, 101, 105, 111, 123]
result = process_numbers(numbers)
print(result)

#18 esep
def flatten_and_filter(lst):
    numbers = []
    def flatten(item):
        if isinstance(item, list):
            for sub_item in item:
                flatten(sub_item)
        else:
            if isinstance(item, (int, float)):
                numbers.append(item)
    flatten(lst)
    filtered = []
    for num in numbers:
        if num > 0 and num % 4 != 0 and abs(num) >= 10:
            filtered.append(num)
    filtered.sort()

    return filtered
test_list = [1, -5, [12, 8, [24, -20, 15]], 7, [100, 4, [36, 9, [44, 50]]], -3]
result = flatten_and_filter(test_list)
print(result)

#19 esep
find_matching_even = lambda list1, list2: [
    list1[i]
    for i in range(min(len(list1), len(list2)))
    if list1[i] == list2[i] and list1[i] % 2 == 0
]
a = [2, 3, 4, 5, 6]
b = [2, 7, 4, 9, 6]
print(find_matching_even(a, b))

#20 esep
def max_subarray_sum(nums, k):
    if len(nums) < k:
        return None

    max_sum = None
    for i in range(len(nums) - k + 1):
        subarray = nums[i:i + k]
        valid = True
        current_sum = 0

        for num in subarray:
            if num <= 0:
                valid = False
                break
            current_sum += num
        if valid:
            if max_sum is None or current_sum > max_sum:
                max_sum = current_sum

    return max_sum


nums = [1, 2, 3, 0, 4, 5, 6, -1, 2, 3]
print(max_subarray_sum(nums, 3))

#21 esep
filter_strings = lambda strings: [
    s.upper()
    for s in strings
    if s.isalpha()
    and len(s) > 4
    and len(set(s.lower())) == len(s)
]
words = ["hello", "world", "python", "code", "abcde", "book", "house"]
print(filter_strings(words))

#22 esep
def group_by_parity_and_sort(nums):
    evens = []
    odds = []

    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    evens.sort()
    odds.sort()
    return evens + odds


nums = [5, 2, 7, 4, 1, 8, 3, 6]
print(group_by_parity_and_sort(nums))

#23 esep
result = lambda nums: [nums[i] for i in range(len(nums))
                      if (lambda n: n>1 and all(n%j!=0 for j in range(2,n)))(i)
                      and nums[i]%2==1
                      and nums[i] > sum(nums)/len(nums)]
numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
print(result(numbers))

#24 esep
def longest_increasing_sublist(nums):
    if not nums:
        return []
    longest = [nums[0]]
    current = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current.append(nums[i])
        else:
            if len(current) > len(longest):
                longest = current.copy()
            current = [nums[i]]
    if len(current) > len(longest):
        longest = current
    return longest
nums = [1, 2, 3, 1, 2, 3, 4, 1, 2]
print(longest_increasing_sublist(nums))

#25 esep
avg_of_sublists = lambda lists: [
    sum(inner) / len(inner)
    for inner in lists
    if len(inner) >= 3
    and sum(inner) % 2 == 0
]

data = [[1, 2, 3], [4, 5, 6, 7], [1, 1, 1], [2, 4, 6, 8], [1, 2]]
print(avg_of_sublists(data))

#26 esep
def remove_duplicates_keep_last(nums):
    seen = set()
    result = []
    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        if num not in seen:
            seen.add(num)
            result.insert(0, num)
    return result
nums = [1, 2, 3, 2, 4, 1, 5, 3]
print(remove_duplicates_keep_last(nums))

#27 esep
top_5_strings = lambda strings: sorted(
    strings,
    key=lambda s: (-len(s), s)
)[:5]
words = ["python", "java", "javascript", "c", "c++", "ruby", "php", "swift"]
print(top_5_strings(words))

#28 esep
def moving_average(nums, k):
    if len(nums) < k:
        return []
    result = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]
        valid = True
        for num in window:
            if num < 0:
                valid = False
                break
        if valid:
            avg = sum(window) / k
            result.append(avg)
    return result
nums = [1, 2, 3, 4, -1, 5, 6, 7, 8]
print(moving_average(nums, 3))

#29 esep
find_unique_large = lambda list1, list2: [
    x
    for x in list1
    if x not in list2
    and x > (sum(list1) / len(list1))
]
a = [10, 20, 30, 40, 50]
b = [20, 40, 60]
print(find_unique_large(a, b))

#30 esep
def analyze_strings_list(words):
    result = []
    seen = set()
    for word in words:
        has_digit = False
        for char in word:
            if char.isdigit():
                has_digit = True
                break
        if has_digit:
            continue
        if len(word) % 2 == 0:
            processed = word[::-1]
        else:
            processed = word.upper()
        if processed not in seen:
            seen.add(processed)
            result.append(processed)
    return result
words = ["hello", "world", "abc123", "python", "hello", "world", "test", "code"]
result = analyze_strings_list(words)
print(result)

#1 esep
def invert_unique(d):
    result = {}
    for key, value in d.items():
        if value not in result:
            result[value] = []
        key_already_exists = False
        for existing_key in result[value]:
            if existing_key == key:
                key_already_exists = True
                break
        if key_already_exists == False:
            result[value].append(key)
    return result
d = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 1}
result = invert_unique(d)
print(result)

#2 esep
filter_set = lambda s: {
    x for x in s
    if x > (sum(s) / len(s))
    and x % 2 != 0
    and x % 5 != 0
}
numbers = {1, 3, 5, 7, 9, 10, 12, 15, 20, 21, 23, 25}
print(filter_set(numbers))

#3 esep
def merge_dicts_sum(d1, d2):
    result = {}
    for key, value in d1.items():
        result[key] = value
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 5, "c": 15, "d": 40, "e": 50}
print(merge_dicts_sum(d1, d2))

#4 esep
def filter_sets(sets_list):
    result = []
    for s in sets_list:
        if len(s) <= 3:
            continue
        has_negative = False
        for num in s:
            if num < 0:
                has_negative = True
                break
        if has_negative:
            continue
        return result

#5 esep
sort_keys = lambda dictionary: sorted(
    dictionary.keys(),
    key=lambda key: (
        -dictionary[key],
        key
    )
)[:5]
student_grades = {
    'Айгүл': 95,
    'Бауыржан': 82,
    'Гүлнар': 95,
    'Дәурен': 78,
    'Ерлан': 92,
    'Жанар': 82,
    'Зере': 88
}

result = sort_keys(student_grades)
print(result)

#6 esep
def deep_sum(d):
    total = 0
    for value in d.values():
        if isinstance(value, (int, float)):
            total += value

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, (int, float)):
                    total += item

        elif isinstance(value, dict):
            total += deep_sum(value)

    return total
data = {
    "a": 10,
    "b": [1, 2, 3, 4],
    "c": {
        "x": 5,
        "y": [6, 7, 8],
        "z": {
            "p": 9,
            "q": 10
        }
    },
    "d": "hello",
    "e": 15
}
print(deep_sum(data))

#7 esep
even_symmetric_difference = lambda set1, set2: {x for x in (set1 ^ set2) if x % 2 == 0}
A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8, 9}
result = even_symmetric_difference(A, B)
print(result)

#8 esep
def sort_dict_by_value_length(d):
    items = []
    for key, value in d.items():
        items.append((key, value))
    sorted_items = sorted(items, key=lambda x: (len(x[1]), x[0]))

    return sorted_items

data = {
    "apple": "fruit",
    "car": "vehicle",
    "python": "snake",
    "book": "reading",
    "dog": "animal"
}
print(sort_dict_by_value_length(data))

#9 esep
def common_elements_all(sets_list):
    if len(sets_list) == 0:
        return set()
    result = sets_list[0].copy()
    for s in sets_list[1:]:
        result = result & s
        if len(result) == 0:
            break
    return result
sets = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}, {4, 5, 6, 7}]
result = common_elements_all(sets)
print(result)

#10 esep
filter_dict = lambda d: {k: sorted([x for x in v if x % 2 == 1])
                         for k, v in d.items()
                         if len([x for x in v if x % 2 == 1]) > 0}
data = {
    'a': [1, 2, 3, 4, 5],
    'b': [2, 4, 6, 8],
    'c': [1, 3, 5, 7],
    'd': [10, 11, 12, 13],
    'e': []
}
result = filter_dict(data)
print(result)

#11 esep
def group_by_length(words):
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = [word]
        else:
            if word not in result[length]:
                result[length].append(word)
    return result
words = ["cat", "dog", "apple", "cat", "book", "pen", "pencil", "dog", "tree"]
print(group_by_length(words))

#12 esep
filter_strings = lambda strings: {
    s for s in strings
    if s.isalpha()
    and len(s) > 4
    and len(set(s)) == len(s)
}
words = {"hello", "world", "abc", "python", "book", "tree", "12345", "house", "apple"}
result = filter_strings(words)
print(result)

#13 esep
def invert_dict_strict(d):
    value_count = {}
    for key, value in d.items():
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1
    result = {}
    for key, value in d.items():
        if value_count[value] == 1:
            result[value] = key
    return result
d = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 3,
    "e": 2,
    "f": 4,
    "g": 5
}
print(invert_dict_strict(d))

#14 esep
def top_k_frequent(nums, k):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    sorted_nums = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    result = set()
    for i in range(min(k, len(sorted_nums))):
        result.add(sorted_nums[i][0])
    return result
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
print(top_k_frequent(nums, 2))

#15 esep
filter_dict = lambda d: {k: v for k, v in d.items()
                         if v >= (sum(d.values()) / len(d))
                         and v % 2 == 1}
data = {'a': 10, 'b': 15, 'c': 20, 'd': 25, 'e': 30, 'f': 35, 'g': 40}
result = filter_dict(data)
print(result)

#16 esep
def update_counts(d, items):
    result = d.copy()
    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
counter = {"apple": 3, "banana": 2, "orange": 1}
new_items = ["apple", "banana", "grape", "apple", "kiwi"]
print(update_counts(counter, new_items))

#17 esep
get_elements = lambda set1, set2, set3: (set1 & set2) - set3
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {5, 6, 7, 9, 10}
result = get_elements(A, B, C)
print(result)

#18 esep
def sort_dict_by_value_sum(d):
    sums = {}
    for key, value_list in d.items():
        total = 0
        for num in value_list:
            total += num
        sums[key] = total
    sorted_items = sorted(sums.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items
data = {
    "a": [1, 2, 3, 4],
    "b": [5, 5, 5],
    "c": [10, 20],
    "d": [2, 4, 6, 8],
    "e": [1, 3, 5, 7, 9]
}
print(sort_dict_by_value_sum(data))

#19 esep
def filter_by_digit_sum(nums):
    result = set()
    for num in nums:
        if num % 2 == 0:
            continue
        digit_sum = 0
        n = abs(num)
        while n > 0:
            digit_sum += n % 10
            n //= 10
        if digit_sum % 2 == 0:
            result.add(num)
    return result
numbers = {123, 456, 789, 111, 222, 333, 444, 555, 666, 777, 888, 999}
result = filter_by_digit_sum(numbers)
print(result)

#20 esep
sort_keys = lambda d: sorted(d.keys(), key=lambda k: (d[k], len(k)))[:3]
data = {
    'apple': 50,
    'banana': 30,
    'kiwi': 30,
    'pear': 40,
    'grape': 20,
    'date': 20
}
result = sort_keys(data)
print(result)

#21 esep
def count_leaf_values(d):
    count = 0
    for key, value in d.items():
        if type(value) == int or type(value) == float:
            count = count + 1
        elif type(value) == list:
            for item in value:
                if type(item) == int or type(item) == float:
                    count = count + 1
                elif type(item) == dict:
                    count = count + count_leaf_values(item)
        elif type(value) == dict:
            count = count + count_leaf_values(value)
    return count
data = {
    'a': 10,
    'b': [1, 2, 3],
    'c': {
        'd': 20,
        'e': [4, 5],
        'f': {
            'g': 30
        }
    },
    'h': [6, {'i': 40}, 7]
}
result = count_leaf_values(data)
print(f"Барлық сандар саны: {result}")

#22 esep
filter_by_second_set = lambda A, B: {
    x for x in A
    if x > (sum(B) / len(B))
    and x not in B
}
A = {10, 15, 20, 25, 30, 35, 40}
B = {5, 10, 15, 20, 25, 45}
print(filter_by_second_set(A, B))

#23 esep
def group_by_last_letter(words):
    result = {}
    for word in words:
        if not word:
            continue
        last_letter = word[-1].lower()
        if last_letter not in result:
            result[last_letter] = [word]
        else:
            if word not in result[last_letter]:
                result[last_letter].append(word)
    return result
words = ["cat", "dog", "bat", "cat", "egg", "bird", "fish", "dog", "hand"]
print(group_by_last_letter(words))

#24 esep
def union_of_filtered_sets(sets_list):
    result = set()
    for s in sets_list:
        for num in s:
            if num > 10 and num % 2 != 0:
                result.add(num)
    return result
sets = [
    {5, 8, 12, 15, 20, 21},
    {3, 7, 11, 13, 17, 19},
    {2, 4, 6, 8, 10, 12},
    {9, 14, 16, 18, 22, 23, 25}
]
print(union_of_filtered_sets(sets))

#25 esep
calculate_products = lambda d: {
    key: __import__('functools').reduce(lambda x, y: x * y, [n for n in values if n > 0], 1)
    for key, values in d.items()
    if any(n > 0 for n in values)
}
data = {
    'a': [1, 2, 3, -1, -2],
    'b': [-5, -10, -15],
    'c': [4, 5, 6],
    'd': [7, -8, 9],
    'e': []
}
result = calculate_products(data)
print(result)

#26 esep
def remove_elements_with_common_digits(s):
    digit_count = {}
    for num in s:
        digits = set(str(abs(num)))
        for digit in digits:
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1
    result = set()
numbers = {12, 23, 34, 45, 123, 456, 78, 89}
print(remove_elements_with_common_digits(numbers))

#27 esep
filter_dict = lambda d: {k: v for k, v in d.items()
                         if (lambda n: n > 1 and all(n % i != 0 for i in range(2, n)))(v)
                         and len(k) % 2 == 1}
data = {
    'a': 2,
    'bb': 3,
    'ccc': 4,
    'dddd': 5,
    'e': 7,
    'ff': 11,
    'ggg': 13,
    'h': 17,
    'i': 19,
    'jj': 23
}
result = filter_dict(data)
print(result)

#28 esep
def sorted_unique_chars(strings):
    unique_chars = set()
    for s in strings:
        for ch in s:
            if ch.isalpha():
                unique_chars.add(ch)
    return sorted(unique_chars)
texts = ["Hello123", "World 456", "Python!", "Test 789"]
result = sorted_unique_chars(texts)
print(result)

#29 esep
sort_by_last_digit = lambda d: [
    key for key, _ in sorted(
        d.items(),
        key=lambda x: (x[1] % 10, x[0])
    )
]
data = {
    "apple": 45,
    "banana": 32,
    "cherry": 45,
    "date": 21,
    "elderberry": 37,
    "fig": 28,
    "grape": 33
}
print(sort_by_last_digit(data))

#30 esep
def partition_by_sum_parity(s):
    jup = set()
    taq = set()
    for san in s:
        kosyndy = 0
        for digit in str(abs(san)):
            kosyndy += int(digit)
        if kosyndy % 2 == 0:
            jup.add(san)
        else:
            taq.add(san)
    return (jup, taq)
sandar = {12, 23, 34, 101, 112}
jup, taq = partition_by_sum_parity(sandar)
print("Жұп:", jup)
print("Тақ:", taq)

#31 esep
filter_lists = lambda d: {
    key: words
    for key, words in d.items()
    if len(set(words)) == len(words) and all(len(w) > 3 for w in words)
}
data = {
    "a": ["apple", "banana", "cat"],
    "b": ["book", "pen", "book"],
    "c": ["house", "tree", "flower"]
}
print(filter_lists(data))

#32 esep
def pairwise_intersections(sets_list):
    if len(sets_list) < 2:
        return []
    result = []
    for i in range(len(sets_list) - 1):
        ortak = set()
        for x in sets_list[i]:
            if x in sets_list[i + 1]:
                ortak.add(x)
        result.append(ortak)
    return result
sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
print(pairwise_intersections(sets))

#33 esep
filter_by_avg = lambda d: {k: v for k, v in d.items()
                           if (sum(v) / len(v)) >
                           (sum(sum(lst) for lst in d.values()) /
                            sum(len(lst) for lst in d.values()))}
data = {
    'a': [10, 20, 30],
    'b': [5, 10, 15],
    'c': [25, 30, 35],
    'd': [1, 2, 3],
    'e': [40, 50, 60]
}
result = filter_by_avg(data)
print(result)

#34 esep
def top_k_smallest_unique(nums, k):
    biregey = set(nums)
    sorted_nums = sorted(biregey)
    result = set()
    for i in range(min(k, len(sorted_nums))):
        result.add(sorted_nums[i])
    return result
nums = [5, 2, 8, 2, 3, 5, 1, 9]
print(top_k_smallest_unique(nums, 3))

#35 esep
filter_dict = lambda d: {
    key: value
    for key, value in d.items()
    if value % 3 != 0 and len(key) % 2 != 0
}
data = {
    "a": 4,
    "bb": 6,
    "ccc": 5,
    "d": 9
}
print(filter_dict(data))

#36 esep
def all_subsets_of_size_k(s, k):
    if k == 0:
        return [set()]
    if not s or k > len(s):
        return []
    elements = list(s)
    first = elements[0]
    rest = set(elements[1:])
    without_first = all_subsets_of_size_k(rest, k)
    with_first = all_subsets_of_size_k(rest, k - 1)
    for subset in with_first:
        subset.add(first)
    return without_first + with_first
s = {1, 2, 3, 4}
k = 2
result = all_subsets_of_size_k(s, k)
print(f"{s} жиынының {k} өлшемді подмножествалары:")
for subset in result:
    print(f"  {subset}")

#37 esep
def fact(n):
    if n <= 1:
        return 1
    f = 1
    for i in range(2, n+1):
        f *= i
    return f
replace_factorial = lambda d: {k: fact(v) if v < 6 else v for k, v in d.items()}
data = {"a": 3, "b": 5, "c": 7, "d": 4}
print(replace_factorial(data))

#38 esep
def multi_symmetric_difference(sets_list):
    count = {}
    for s in sets_list:
        for elem in s:
            count[elem] = count.get(elem, 0) + 1
    result = set()
    for elem, cnt in count.items():
        if cnt % 2 == 1:
            result.add(elem)
    return result
sets = [
    {1, 2, 3, 4},
    {3, 4, 5, 6},
    {5, 6, 7, 8}
]
print(multi_symmetric_difference(sets))

#39 esep
VOWELS = set("аәеёиоөуұыіэюяaeiou")
sort_keys = lambda d: sorted(
    d.keys(),
    key=lambda k: (
        -sum(1 for ch in k.lower() if ch in VOWELS),
        -d[k]
    )
)
data = {
    'apple': 10,
    'banana': 20,
    'orange': 15,
    'pear': 25,
    'grape': 5,
    'apricot': 30
}
result = sort_keys(data)
print(result)

#40 esep
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
    'a!b@c#': 9
}
result = analyze_dict_keys(d)
print(sorted(result))

#Большая комплексная задача: "Анализ текстовой базы данных студентов"
import string
from collections import defaultdict
def analyze_students(data):
    PUNCT = set(string.punctuation)
    VOWELS = set("аәеёиоөуұыіэюяaeiou")
    students = []
    for s in data:
        if not any(ch.isdigit() for ch in s["name"]):
            students.append({
                "name": s["name"].title(),
                "grades": s["grades"][:],
                "comments": s["comments"][:]
            })
    for s in students:
        processed = []
        for g in s["grades"]:
            if g <= 0:
                continue
            if g % 2 and g < 10:
                processed.append(sum(int(d) for d in str(g)))
            elif g % 2 == 0 and g >= 10:
                processed.append(g * g)
            else:
                processed.append(g)
        s["processed_grades"] = processed
    for s in students:
        text = " ".join(s["comments"])
        clean = "".join(ch for ch in text if ch not in PUNCT)
        words = set(w.lower() for w in clean.split()
                    if len(w) >= 4 and w.lower() != w.lower()[::-1])
        s["unique_words"] = words
        s["word_vowels"] = {ch for w in words for ch in w if ch in VOWELS}
    word_counts = defaultdict(int)
    for s in students:
        for w in s["unique_words"]:
            word_counts[w] += 1
    word_counts = {w: c for w, c in word_counts.items() if c >= 2}
    word_counts = dict(sorted(word_counts.items(), key=lambda x: (-x[1], x[0])))
    all_vowels = set().union(*(s["word_vowels"] for s in students))
    students_by_avg = sorted(
        students,
        key=lambda s: (-(sum(s["processed_grades"]) / len(s["processed_grades"]) if s["processed_grades"] else 0),
                       s["name"])
    )
    students_by_avg = [s["name"] for s in students_by_avg]
    by_length = defaultdict(list)
    seen = set()
    for s in students:
        if s["name"] not in seen:
            seen.add(s["name"])
            by_length[len(s["name"])].append(s["name"])
    return {
        "students": [{"name": s["name"], "processed_grades": s["processed_grades"]} for s in students],
        "word_counts": word_counts,
        "all_vowels": all_vowels,
        "students_by_avg": students_by_avg,
        "students_by_name_length": dict(by_length)
    }
#Большая комплексная задача: "Анализ заказов онлайн-магазина"
import string
from collections import defaultdict
def analyze_orders(orders):
    PUNCT = set(string.punctuation)
    VOWELS = set("аәеёиоөуұыіэюяaeiou")
    print("=" * 80)
    print("1-ҚАДАМ: Фильтрация заказов и клиентов")
    print("=" * 80)
    filtered_orders = []
    for order in orders:
        customer = order["customer"]
        has_digit = False
        for ch in customer:
            if ch.isdigit():
                has_digit = True
                break
        if has_digit:
            print(f"  Заказ {order['order_id']}: клиент '{customer}' - цифр бар, өткіземіз")
            continue
        parts = customer.split('_')
        title_parts = [p[0].upper() + p[1:].lower() for p in parts if p]
        new_customer = '_'.join(title_parts)
        print(f"  Заказ {order['order_id']}: клиент '{customer}' -> '{new_customer}'")
        new_order = {
            "order_id": order["order_id"],
            "customer": new_customer,
            "items": order["items"].copy(),
            "notes": order["notes"].copy()
        }
        filtered_orders.append(new_order)
    print("\n" + "=" * 80)
    print("2-ҚАДАМ: Обработка товаров в заказах")
    print("=" * 80)
    for order in filtered_orders:
        print(f"\nЗаказ {order['order_id']}:")
        processed_items = []
        for item in order["items"]:
            name = item["name"]
            price = item["price"]
            quantity = item["quantity"]
            print(f"  Товар: {name}, бағасы: {price}, саны: {quantity}")
            if price <= 0:
                print(f"     Баға <= 0, өткіземіз")
                continue
            new_price = price
            if price > 100 and quantity > 1:
                new_price = price * quantity
                print(f"    price>100 және quantity>1: {price} * {quantity} = {new_price}")
            if quantity % 2 == 1:
                digit_sum = 0
                n = int(price)
                while n > 0:
                    digit_sum += n % 10
                    n //= 10
                new_price += digit_sum
                print(f"    quantity тақ: +{digit_sum} (цифрлар қосындысы) = {new_price}")
            processed_items.append({
                "name": name,
                "price": round(new_price, 2),
                "quantity": quantity
            })
            print(f"  Қосылды: {name} -> бағасы: {round(new_price, 2)}")
        order["processed_items"] = processed_items
        total = sum(item["price"] for item in processed_items)
        print(f"  Заказ жиыны: {len(processed_items)} товар, жалпы сумма: {round(total, 2)}")
    print("\n" + "=" * 80)
    print("3-ҚАДАМ: Анализ заметок к заказу")
    print("=" * 80)
    all_order_words = []
    for order in filtered_orders:
        print(f"\nЗаказ {order['order_id']} (клиент: {order['customer']}):")
        print(f"  Заметки: {order['notes']}")
        all_notes = " ".join(order["notes"])
        clean_text = ""
        for ch in all_notes:
            if ch not in PUNCT:
                clean_text += ch
        words = clean_text.split()
        unique_words = set()
        for word in words:
            word_lower = word.lower()
            if len(word_lower) >= 4 and word_lower != word_lower[::-1]:
                unique_words.add(word_lower)
        order["unique_words"] = unique_words
        all_order_words.append(unique_words)
        word_vowels = set()
        for word in unique_words:
            for ch in word:
                if ch in VOWELS:
                    word_vowels.add(ch)
        order["word_vowels"] = word_vowels
        print(f"  Уникальды сөздер: {sorted(unique_words)}")
        print(f"  Дауыстылар: {sorted(word_vowels)}")
    print("\n" + "=" * 80)
    print("4-ҚАДАМ: Глобальный анализ по всем заказам")
    print("=" * 80)
    word_counts = defaultdict(int)
    for i, words in enumerate(all_order_words):
        print(f"\nЗаказ {filtered_orders[i]['order_id']} сөздері: {sorted(words)}")
        for word in words:
            word_counts[word] += 1
    filtered_word_counts = {word: count for word, count in word_counts.items() if count >= 2}
    sorted_words = sorted(filtered_word_counts.items(), key=lambda x: (-x[1], x[0]))
    word_counts_dict = dict(sorted_words)
    print(f"\nГлобальды сөздер (кемінде 2 заказда):")
    for word, count in word_counts_dict.items():
        print(f"  '{word}': {count} заказ")
    print("\n" + "=" * 80)
    print("5-ҚАДАМ: Сводные данные по товарам")
    print("=" * 80)
    all_products = set()
    for order in filtered_orders:
        for item in order["processed_items"]:
            all_products.add(item["name"])
    print(f"\nУникальды товарлар: {sorted(all_products)}")
    order_totals = []
    for order in filtered_orders:
        total = sum(item["price"] for item in order["processed_items"])
        order_totals.append((order["order_id"], total))
        print(f"  {order['order_id']}: жалпы сумма = {round(total, 2)}")
    sorted_orders = sorted(order_totals, key=lambda x: (-x[1], x[0]))
    orders_by_total = [order_id for order_id, _ in sorted_orders]
    print(f"\nСұрыпталған заказдар: {orders_by_total}")
    orders_by_item_count = defaultdict(list)
    seen = set()
    for order in filtered_orders:
        order_id = order["order_id"]
        item_count = len(order["processed_items"])
        if order_id not in seen:
            seen.add(order_id)
            orders_by_item_count[item_count].append(order_id)
    for count in orders_by_item_count:
        orders_by_item_count[count].sort()
    print(f"\nТовар саны бойынша заказдар:")
    for count, ids in sorted(orders_by_item_count.items()):
        print(f"  {count} товар: {ids}")
    print("\n" + "=" * 80)
    print("6-ҚАДАМ: Нәтижені құрастыру")
    print("=" * 80)
    all_vowels = set()
    for order in filtered_orders:
        all_vowels.update(order["word_vowels"])
    result = {
        "orders": [
            {
                "order_id": o["order_id"],
                "customer": o["customer"],
                "processed_items": o["processed_items"]
            }
            for o in filtered_orders
        ],
        "word_counts": word_counts_dict,
        "all_vowels": all_vowels,
        "unique_products": all_products,
        "orders_by_total": orders_by_total,
        "orders_by_item_count": dict(orders_by_item_count)
    }
    return result
test_orders = [
    {
        "order_id": "A123",
        "customer": "john_doe42",
        "items": [
            {"name": "Laptop", "price": 999.99, "quantity": 1},
            {"name": "Mouse", "price": 25, "quantity": 2}
        ],
        "notes": ["Deliver ASAP", "fragile package", "handle with care"]
    },
    {
        "order_id": "B456",
        "customer": "alice_smith",
        "items": [
            {"name": "Monitor", "price": 299.99, "quantity": 2},
            {"name": "Keyboard", "price": 45.50, "quantity": 1},
            {"name": "Mouse", "price": 25, "quantity": 3}
        ],
        "notes": ["office delivery", "fragile items", "signature required"]
    },
    {
        "order_id": "C789",
        "customer": "bob_jones",
        "items": [
            {"name": "Laptop", "price": 999.99, "quantity": 2},
            {"name": "Mouse", "price": -10, "quantity": 1},  # Теріс баға
            {"name": "Headphones", "price": 89.99, "quantity": 0}  # Нөлдік саны
        ],
        "notes": ["urgent delivery", "handle with care"]
    },
    {
        "order_id": "D012",
        "customer": "charlie_brown",
        "items": [
            {"name": "Tablet", "price": 399.99, "quantity": 1},
            {"name": "Case", "price": 29.99, "quantity": 2}
        ],
        "notes": ["fragile package", "deliver after 5pm", "signature required"]
    }
]
print("=" * 80)
print("БАСТАПҚЫ ЗАКАЗДАР:")
print("=" * 80)
for order in test_orders:
    print(f"Заказ {order['order_id']}: клиент {order['customer']}")
    print(f"  Товарлар: {[(item['name'], item['price'], item['quantity']) for item in order['items']]}")
    print(f"  Заметки: {order['notes']}")
    print()
result = analyze_orders(test_orders)
print("\n" + "=" * 80)
print("СОҢҒЫ НӘТИЖЕ:")
print("=" * 80)
print(f"Өңделген заказдар саны: {len(result['orders'])}")
print(f"Уникальды сөздер: {result['word_counts']}")
print(f"Барлық дауыстылар: {sorted(result['all_vowels'])}")
print(f"Уникальды товарлар: {sorted(result['unique_products'])}")
print(f"Заказдар (сумма бойынша): {result['orders_by_total']}")
print(f"Заказдар (товар саны бойынша): {result['orders_by_item_count']}")
print("\nӨҢДЕЛГЕН ЗАКАЗДАР:")
for order in result["orders"]:
    total = sum(item["price"] for item in order["processed_items"])
    print(f"  {order['order_id']} ({order['customer']}): {order['processed_items']} | Жалпы: {round(total, 2)}")