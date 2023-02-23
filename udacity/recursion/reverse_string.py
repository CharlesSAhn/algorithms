

def reverse_string(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """

    if len(input) <= 0:
        return ""

    first = input[0]
    rest = slice(1, None)
    sub_string = input[rest]
    reverse = reverse_string(sub_string)

    return reverse + first



print(reverse_string("abc"))