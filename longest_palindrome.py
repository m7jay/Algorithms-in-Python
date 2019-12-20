from typing import Set
def longest_palindrome(source:str)-> str:
    palidromes = set()
    #odd palindromes
    for i in range(1, len(source)):
        start = i 
        index = 1
        while start < len(source)-1 and index < len(source)//2 - 1:
##            print(start, index)
            if source[start - index] == source[start + index]:
                index += 1
            elif index > 1:
                palidromes.add(source[(start - index-1) : (start + index+1)])
    print(palidromes)

if __name__ == "__main__":
    longest_palindrome("abacdcafg")