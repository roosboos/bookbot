def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents 
    
from stats import count_words
from stats import count_char
from stats import report

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    char_count = count_char(book_text)
    sorted_chars = report(char_count)
    
    # Print the formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count, but only if it's alphabetical
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    
    print("============= END ===============")



if __name__ == "__main__":
    main()