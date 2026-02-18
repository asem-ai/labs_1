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