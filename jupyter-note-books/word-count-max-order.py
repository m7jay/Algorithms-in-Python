import sys
import string
def word_count():
    words = {}
    strip = string.whitespace + string.punctuation + string.digits + "\"'"
    for filename in sys.argv[1:]:
        with open(filename) as file:
            for line in file:
                for word in line.lower().split():
                    word = word.strip(strip)
                    if len(word)>2:
                        words[word] = words.get(word, 0) + 1 #find the word in the dictionary if not present returns 0
        if words:
            print("Max Values:")
            max_val = max(words.values())
            key_list = words.keys()
            for i in key_list:
                if words[i] == max_val:
                    print(i, max_val)        
            print("Word Count in alphabetical order:")
            for w in sorted(words):
                print("{}:{}".format(w, words[w]))
        else:
            print("Empty file- ", filename)

#sys.argv[1] = "test.txt"
word_count()