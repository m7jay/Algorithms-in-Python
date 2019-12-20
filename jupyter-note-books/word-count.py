
# coding: utf-8

# In[7]:


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
        for w in sorted(words):
            print("{}:{}".format(w, words[w]))

word_count()