def get_book_text(book):
    with open("books/" + book) as f:
        contents = f.read()
    return contents
























def main(book):
    from stats import get_num_words
    get_num_words(book)
main("frankenstein.txt")
