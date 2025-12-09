def get_book_text(book):
    with open(book) as f:
        contents = f.read()
    return contents












def printer(part):
    if part == 1:
        print("============ BOOKBOT ============")
        print("Analyzing book found at " +sys.argv[1])
        print("----------- Word Count ----------")
    if part == 2:
        print("--------- Character Count -------")
    if part == 3:
        print("============= END ===============")





from stats import get_num_words, get_num_characters, sort, helper
import sys



def main():

    if len(sys.argv) >= 2:
        filepath = sys.argv[1]
        text = get_book_text(sys.argv[1])
        printer(1)
        print(get_num_words(text))
        printer(2)
        sorted_list = sort(get_num_characters(text))
        for item in sorted_list:
            print(f"{item['char']}: {item['num']}")
        printer(3)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()