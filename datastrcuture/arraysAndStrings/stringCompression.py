'''
Questions:  Implement a method to perform basic string compression using the counts of repeated characters.

aabcccccaaa -> a2b1c5a3

if the compressed string would not become smaller than the original string, your method should return the original string.
you can assume the string has only uppercase  and lower case.

Question:
- case sensitive?
- can I use extra space?

approach
- two pointers
- pointer1: iterate through each character
- pointer2: count repeated characters
- create an emtpy list
- if unqinue, append the character to the list.
- if next character is same, count until it is not,
    use the pointer1 to track the current position and pointer2 to track the repetition.
- append the list and update the pointers.
    - pointer1 = pointer2 + 1
    - pointer2 += pointer2 + 1

Run time:
- N  + N-x

'''

def compression(word):

    pointer1 = 0
    pointer2 = 1

    compressed_word = []

    if len(word) < 1:
        return ""

    while (pointer1 < len(word)):

        if pointer2 < len(word):
            while (word[pointer1] == word[pointer2]):  # a == a
                pointer2 += 1
                if pointer2 == len(word):
                    break# pointer2 = 2

        compressed_word.append(word[pointer1])                               #[a]
        compressed_word.append(str(pointer2 - pointer1))                          #[a2]
        pointer1 = pointer2                                                  # pointer= 2
        pointer2 += 1



    return "".join(compressed_word)


"""
input = "aa"


"""
print(compression('aa'))
print(compression('aabcccccaaa'))
print(compression('a'))
print(compression(''))