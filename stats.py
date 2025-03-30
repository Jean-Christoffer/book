def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def get_book_text_length(book):
    book_length = len(book.split())
    return book_length


def num_characters(book):
    characters = list(book)
    character_dictonary = {}

    for i in range(len(characters)):
        char = characters[i].lower()
        if char not in character_dictonary:
            character_dictonary[char] = 1
        else:
            character_dictonary[char] += 1
    return character_dictonary


def generate_report(book_dictonary):
    list_of_dictonaries = []

    for key, value in book_dictonary.items():
        dict = {"char": key, "count": value}
        list_of_dictonaries.append(dict)

    list_of_dictonaries.sort(reverse=True, key=lambda x: x["count"])

    return list_of_dictonaries
