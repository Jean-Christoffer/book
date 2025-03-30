from stats import get_book_text, get_book_text_length, num_characters, generate_report
from sys import argv, exit

def main():
    
    args = argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book = get_book_text(args[1])
    book_length = get_book_text_length(book)
    amount_of_characters = num_characters(book)
    report = generate_report(amount_of_characters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {book_length} total words")
    print("--------- Character Count -------")
    for char_dict in report:
        char = char_dict["char"]
        char_count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {char_count}")
    print("============= END ===============")


main()
