def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(char_dict):
    sorted_list=[]
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

