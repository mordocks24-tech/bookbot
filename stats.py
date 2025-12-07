
def get_num_words(text):
    with open("books/" + text) as f:
        contents = f.read()
    words = contents.split()
    word_count = str(len(words))

    print("Found " + (word_count) + " total words")



def get_num_characters():
    





    return