'''
A palindrome is a word that is the reverse of itself—that is, it is the same word when read forwards and backwards.

For example:

"madam" is a palindrome
"abba" is a palindrome
"cat" is not
"a" is a trivial case of a palindrome

'''


def is_palindrome(input):

    if len(input) <= 1:
        return True

    first = input[0]
    last = input[-1]

    if first != last:
        return False

    sliceobj = slice(1, len(input)-1)
    return is_palindrome(input[sliceobj])


print(is_palindrome('madam'))
print(is_palindrome('abba'))
print(is_palindrome('cat'))
print(is_palindrome('d'))