def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_char(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else: 
            char_counts[char] = 1
    return char_counts