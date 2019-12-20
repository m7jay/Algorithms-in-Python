def longest_palindrome(source:str)-> str:
    palidromes = []
    #odd palindromes
    for i in range(1, len(source)):
        start = i
        index = 1
        while start < len(source):
            if source[start - index] == source[start + index]:
                index += 1
            else:
                palidromes.append(source[(start - index) : (start + index)])
    print(palidromes)

if __name__ == "__main__":
    longest_palindrome("abacdcafg")