def main():    
    path = "books/frankenstein.txt"
    text = read_book_text(path)
    word_count = count_book_words(text)
    character_count = count_characters(text)
    sorted_list = sorted_list_of_dicts(character_count)
    generate_report(sorted_list, word_count)

def read_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_book_words(text):
    split_arr = text.split()
    return len(split_arr)
    
def count_characters(text):
    char_dict = {}
    lower_text = text.lower()
    for c in lower_text:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def sorted_list_of_dicts(char_dict):
    new_dict = {}
    for c in char_dict:
        if c.isalpha():
            new_dict[c] = char_dict[c]
    new_list = []

    for key in new_dict:
        new_list.append({"char":key, "num": new_dict[key]})
        
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(dict):
    return dict["num"]

def generate_report(sorted_list, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print(" ")
    for d in sorted_list:
        print(f"The {d["char"]} character was found {d["num"]} times")
    print("--- End report ---")
    

# first I have to organize the data, and make the dictionary a list of dictionaries

main()
    