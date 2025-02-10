def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    char_count = count_chatracters(file_contents)
    word_count = count_words(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for char in char_count:
        if char.isalpha():
            print(f"The '{char}' character was found {char_count[char]} times")

    print("--- End report ---")

def count_chatracters(text):
    count_dictionary = {}
    lower_text = text.lower()
    for char in lower_text:
        count_dictionary[char] = count_dictionary.get(char, 0) + 1
    return count_dictionary

def count_words(text):
    word_count =len(text.split())
    return word_count
        
main()