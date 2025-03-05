def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def counting_words(file_contents):
    words = file_contents.split()
    return len(words)

def main():
    path_to_file = 'books/frankenstein.txt'  # Specify the path to your book file
    book_text = get_book_text(path_to_file)
    num_words = counting_words(book_text)
    print(f"{num_words} words found in the document")

main()