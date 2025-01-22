def main():
    book_path = "books/frankenstein.txt"
    text = read_text(book_path)
    word_count = count_words(text)
    char_dict = count_characters(text)
    characters = sort_characters(char_dict)
    create_report(book_path, word_count, characters)

# Converts file into string
def read_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

# Returns number of words in text
def count_words(text):
    words = text.split()
    word_count = 0
    for i in range (0,len(words)):
        word_count += 1
    return word_count

# Returns number of each alphabetical character as a dictionary
def count_characters(text):
    lowercase_text = text.lower()
    characters = list(lowercase_text)
    char_dict = {}
    for char in characters:
        if(char.isalpha() == True):
            if(char not in char_dict):
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

# Define how to sort
def sort_on(characters):
    for char in characters:
        return characters[char]

# Returns a sorted dictionary by reverse value
def sort_characters(char_dict):
    sorted_dict = {}
    characters = [{key:value} for key, value in char_dict.items()]
    characters.sort(reverse=True, key=sort_on)
    for char in characters:
        sorted_dict.update(char)
    return sorted_dict

# Prints a report of the text
def create_report(text, word_count, characters):
    print(f"--- Begin new report of {text} ---\n")
    print(f"{word_count} words found in the document\n\n")
    for char in characters:
        print(f"The '{char}' character was found {characters[char]} times\n")
    print("--- End report ---")

main()