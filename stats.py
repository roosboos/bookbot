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

def report(char_counts):
    chars_list = []
    
    for char, count in char_counts.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)
    def sort_on(dict):
        return dict["count"]
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list