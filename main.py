from stats import get_num_words
from stats import get_num_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)

    print(text)


    print(f"{num_words} words found in the document")

    print(f"{num_characters} characters in the document")




main()



