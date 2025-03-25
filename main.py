def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents 
    
def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    print(f"{word_count} words were found in the document")


if __name__ == "__main__":
    main()