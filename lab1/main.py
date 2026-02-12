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

