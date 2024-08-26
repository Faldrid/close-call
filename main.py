def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_of_chars = count_num_of_chars(text)
    for key in num_of_chars: 
        print(f"The '{key}' character was found {num_of_chars[key]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    words = string.split()
    return len(words)

def count_num_of_chars(string):
    lowercase_string = string.lower()
    dict_of_chars = {'a': 0,'b': 0,'c': 0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    for char in lowercase_string:
        if char in dict_of_chars:
            dict_of_chars[char] += 1
    return dict_of_chars
    
if __name__ == '__main__':
    main()
