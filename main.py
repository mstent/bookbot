def main():
    book_path = "books/frankenstein.txt"
    book_words = get_book_words(book_path)

    print(f"--- Begin report of {book_path} ---")

    # number of words in document
    book_words_number = count_words(book_words)
    if book_words_number != 1:
        print(f"There are {book_words_number} words in the document.")
    else:
        print("There is 1 word in this document.")
    
    # number of times each letter appears in document
    book_character_count = get_times_characters_appear(book_words)
    print("\n")
    for char in book_character_count:
        print(f"The letter '{char["character"]}' was found {char["amount"]} times")

    print("\n--- End Report ---")


def get_book_words(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def get_times_characters_appear(text):
    character_count = {}
    for character in text:
        if character.lower() in character_count:
            character_count[character.lower()] += 1
        else:
            character_count[character.lower()] = 1

    list_of_characters = []
    for char in character_count:
        if char.isalpha():
            analysis = {"character": char, "amount": character_count[char]}
            list_of_characters.append(analysis)
    
    list_of_characters.sort(reverse=True, key=sort_on)
    return list_of_characters

def sort_on(dict):
    return dict["amount"]

main()