def get_num_words(text):
    words = text.split()
    num_words = len(words)

    return num_words

def get_num_characters(text):
    lowercase = text.lower()
    characters = {}
    for char in lowercase:
        if char not in characters:
             characters[char] = 1
        else:
            characters[char] += 1
    return characters