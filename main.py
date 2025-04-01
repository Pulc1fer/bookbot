from stats import get_num_words, get_num_characters, sorted_data
import sys

if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
path = sys.argv[1]


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted_list = sorted_data(num_characters)
    print_report(path, num_words, sorted_list)


def print_report(path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")




main()



