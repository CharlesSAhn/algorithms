
import collections


alphabets = ['a', 'b', 'c', 'ch', 'dd', 'd', 'e', 'f', 'ff', 'g', 'ng', 'h', 'i', 'j', 'l', 'll', 'm', 'n', 'o', 'p', 'ph', 'r', 'rh', 's', 't', 'th', 'u', 'w', 'y']


def sort(words):

	aphabets_index = collections.defaultdict(int)

	for i, char in enumerate(alphabets):
		aphabets_index[char] = i


	words_array = []

	for word in words:

		wordv2 = []
		i = 0
		while i < len(word):
			if word[i:i+2] in aphabets_index:
				wordv2.append(aphabets_index[word[i:i+2]])
				i += 2
			else:
				wordv2.append(aphabets_index[word[i:i+1]])
				i += 1



		words_array.append(wordv2)
	
	words_array.sort()

	sorted__words = []

	for word_array in words_array:
		temp = []
		for index in word_array:
			temp.append(alphabets[index])

		sorted__words.append("".join(temp))

	return sorted__words










print(sort(['abcd', 'abcdd']))
# ['abcdd', 'abcd']
print(sort(['abcd', 'abcdd', 'abcch']))
# ['abcch', 'abcdd', 'abcd']
print(sort(["d", "ddr", "nah", "dd", "dea", "ngah"]))
# ['dd', 'ddr', 'd', 'dea', 'ngah', 'nah']