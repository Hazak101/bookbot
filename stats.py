def counting_words(text):
    words = text.split()
    return len(words)

def counting_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(d):
        return d["count"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "count": num_chars_dict[ch]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list