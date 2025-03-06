from stats import counting_words, counting_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
         return f.read()


def main():
    path_to_file = 'books/frankenstein.txt'  # Specify the path to your book file
    text = get_book_text(path_to_file)
    num_words = counting_words(text)
    num_chars = counting_characters(text)
    print(f"{num_words} words found in the document")
    print(num_chars)

main()