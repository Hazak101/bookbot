from stats import counting_words, counting_characters, chars_dict_to_sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
         return f.read()
    
def print_report(path_to_file, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")





def main():
    path_to_file = 'books/frankenstein.txt'  # Specify the path to your book file
    text = get_book_text(path_to_file)
    num_words = counting_words(text)
    num_chars = counting_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_chars)
    print_report(path_to_file, num_words, chars_sorted_list)

   
    

main()