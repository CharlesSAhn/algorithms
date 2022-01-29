'''
A keypad on a cellphone has alphabets for all numbers between 2 and 9.

You can make different combinations of alphabets by pressing the numbers.

For example, if you press 23, the following combinations are possible:

ad, ae, af, bd, be, bf, cd, ce, cf

Note that because 2 is pressed before 3, the first letter is always an alphabet on the number 2. Likewise, if the user types 32, the order would be

da, db, dc, ea, eb, ec, fa, fb, fc

Given an integer num, find out all the possible strings that can be made using digits of input num. Return these strings in a list.
The order of strings in the list does not matter. However, as stated earlier, the order of letters in a particular string matters.

Performance:
- n
O(3 ^ n * 3)

space:
- 3 ^ n
'''


map = {

    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["i", "g", "h"],
    "5": ["l", "j", "k"],
    "6": ["o", "m", "n"],
    "7": ["r", "p", "q"],
    "8": ["u", "s", "t"],
    "9": ["x", "v", "w"]
}

def combination(input):

    return helper_combination(input, 0)


def helper_combination(input, index):

    if index == len(input):
        return [""]

    small_output = helper_combination(input, index + 1)

    new_list = list()

    for combination in small_output:    # 3^(n-1), 3^(n-2),   ... ,3
        for char in map[input[index]]:  # 3
            new_list.append(char + combination)

    return new_list

print(combination(""))
print(combination("23"))
print(len(combination("354")))