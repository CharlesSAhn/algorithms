


def coprime(a,b):

    if (a==0 or b==0):
        return 0

    if (a==b):
        return a 

    if (a>b):
        return coprime(a-b, b)

    return coprime(a, b-a)



a = 5
b = 6
print(coprime(a,b))


a = 13
b = 7
print(coprime(a,b))


