def count_words(content):
    words_list = content.split()
    return len(words_list)

def count_char(content):
    res = {}
    for char in content.lower():
        if char in res:
            res[char] += 1
        else:
            res[char] = 1
    return res

def format_report(words_count, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    print("\n")
    for char in char_count:
        print(f"The '{char}' character was found {char_count[char]} times")
    print("--- End report ---")



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        words_count = count_words(file_contents)
        char_count = count_char(file_contents)
        format_report(words_count, char_count)

main()
