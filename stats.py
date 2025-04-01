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

def sort_on(d):
    return d["num"]

def sorted_data(char_dict):
    result = []
    for char in char_dict:
        result.append({"char" : char, "num": char_dict[char]})
    result.sort(reverse=True, key=sort_on)
    return result