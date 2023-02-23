from random import randint

'''

Write a function to generate a random number between 1 and 9 with equal probability, 
given a method rand6() that generates a random number between 1 and 6.

'''


def generate():

	x = randint(1,5)

	i = 0
	i = (5 * x) + (x - 5) 

	if i < 22:
		return i % 7 + 1
	return generate()


freq = {}
 
for i in range(100000):
    val = generate()
    freq.setdefault(val, 0)
    freq[val] += 1

print(freq)
for i in range(1, len(freq) + 1):
    print(f'{i} ~ {freq[i] / 1000}%')