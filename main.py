
filename = "books/frankenstein.txt"

def main() :
    with open(filename) as f:
        file_contents = f.read()
    print_report(file_contents)

def print_report(text):
    word_count = wordCount(text)
    char_count = get_char_count(text)

    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document\n")
    sorted_char_counts = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def wordCount(text) :
    words = text.split()
    return len(words)

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
