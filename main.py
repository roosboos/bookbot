def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents 
    
from stats import count_words


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")


if __name__ == "__main__":
    main()