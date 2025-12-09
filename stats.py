
def get_num_words(text):
    words = text.split()
    word_count = str(len(words))
    
    return("Found " + (word_count) + " total words")


def get_num_characters(text):
     num_character_dict = {}
     bloated_list = list(text)


     for letter in bloated_list:
         letter = letter.lower()
         if letter.isalpha():
             if letter in num_character_dict:
                 num_character_dict[letter] += 1
             else:
                 num_character_dict[letter] = 1
     return num_character_dict

def helper(dictionar_parameter):
     # return the numeric count for sorting
     return dictionar_parameter["num"]

def sort(num_character_dict):
     num_character_list = []
     # build a list of dictionaries with explicit keys
     for letter, number in num_character_dict.items():
         num_character_list.append({"char": letter, "num": number})

     # sort by the numeric count (highest first)
     num_character_list.sort(reverse=True, key=helper)

     return num_character_list














