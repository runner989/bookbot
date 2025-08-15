
import sys
from stats import get_num_words

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filename = sys.argv[1]
    with open(filename) as f:
        file_contents = f.read()
    print_report(filename, file_contents)

def print_report(filename, text):
    word_count = get_num_words(text)
    char_count = get_char_count(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_char_counts = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_char_counts:
        # print(f"The '{char}' character was found {count} times")
        print(f"{char}: {count}")
    print("============= END ===============")

def sort_on(dict):
    return dict["num"]

def get_char_count(text):
    chars = {}
    text = text.lower()
    words = text.split() 
    for word in words: 
        for c in word: 
            if c != " " and c.isalpha():
                if c in chars.keys():
                    count = chars[c] + 1
                    chars[c]=count
                else:
                    chars[c]=1    
    return chars

if __name__ == '__main__':
    main()
