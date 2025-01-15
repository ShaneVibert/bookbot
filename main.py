def report(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

        print("--- Begin report of file ---")

        words = text.split()
        word_count = len(words)
        print(f"{word_count} words found in the document\n")

        characters = {}
        lower_case = text.lower()
        for char in lower_case:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

        char_list = [{"character": char, "count": count} for char, count in characters.items()]
        char_list.sort(key=lambda item: item['count'], reverse=True)

        print("Character frequencies:\n")
        for item in char_list:
            if item['character'].isalpha():
                print(f"The '{item['character']}' character was found {item['count']} times")
            else:
                print(f"The character '{item['character']}' was found {item['count']} times")

        print("\n--- End report ---")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: An error occurred while reading the file '{file_path}'.")
