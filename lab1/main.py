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
process = lambda s: " ".join([word.lower() for word in s.split() if sum(1 for ch in word if ch.isupper()) == 1 and not word[0].isupper() and not word[-1].isupper()])
text = "Hello PyThon tEst world"
print(process(text))

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
process = lambda s: [word for word in s.split() if len(word) >= 4 and not any(ch.isdigit() for ch in word) and len(set(word.lower())) == len(word)]
text = "test hello world apple banana"
print(process(text))


#7 esep
def palindrome_words(text):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for p in punctuation:
        text = text.replace(p, ' ')
    words = text.split()
    palindromes = set()
    for word in words:
        if len(word) >= 3 and word.lower() == word.lower()[::-1]:
            palindromes.add(word.lower())
    return sorted(palindromes, key=lambda x: (-len(x), x))
text = "level madam hello civic world"
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
special_words = lambda text: [
    word
    for word in text.split()
    if len(word) > 3
    and word[0].lower() == word[-1].lower()
    and word.lower() != word.lower()[::-1]
]
text = "hello level world madam civic"
print(special_words(text))
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
filter_vowel_words = lambda text: ', '.join(
    word
    for word in text.split()
    if len(set(word.lower())) > 3
    and len(set(c for c in word.lower() if c in 'aeiou')) == len([c for c in word.lower() if c in 'aeiou'])
)
text = "hello world python beauty queue"
print(filter_vowel_words(text))

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
filter_numbers = lambda nums: [
    x ** 2
    for x in nums
    if (x % 3 == 0 or x % 5 == 0)
    and x % 15 != 0
    and len(str(abs(x))) % 2 != 0
]
nums = [3, 5, 15, 9, 10, 30, 25, 100, 7]
print(filter_numbers(nums))
#18 esep
def flatten_and_filter(lst):
    result = []
    def extract_numbers(item):
        if isinstance(item, (int, float)):
            if item > 0 and item % 4 != 0 and item >= 10:
                result.append(item)
        elif isinstance(item, list):
            for elem in item:
                extract_numbers(elem)
    extract_numbers(lst)
    return sorted(result)
data = [1, [-5, 12, [8, 15, [20, -3, 30]]], [4, 7], 25]
print(flatten_and_filter(data))