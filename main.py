def report(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    print("--- Begin report of books/frankenstein.txt ---")

    words = text.split()
    word_count = len(words)
    print(f"{word_count} words found in the document")
    print()

    characters = {}
    lower_case = text.lower()
    for char in lower_case:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    char_list = [{"character": char, "count": count} for char, count in characters.items()]
    char_list.sort(key=lambda item: item['count'], reverse=True)

    for item in char_list:
        if item['character'].isalpha():
            print(f"The '{item['character']}' character was found {item['count']} times")
        else:
            print(f"The character '{item['character']}' was found {item['count']} times")

    print("--- End report---")

# Call the function with the path to your text file
report('books/frankenstein.txt')
