a = {chr(65+i) : 0 for i in range(26)}
n = int(input())

for i in range(n):
	m = list(input().split())
	
	for j in m:
		for k in range(0, len(j)):
			x = ord(j[k])
			if x >= 65 and x <= 90:
				a[chr(x)] += 1
			elif x >= 97 and x <= 122:
				a[chr(x - 97 + 65)] += 1

b = sorted(a.items(), key = lambda d:d[1], reverse = True)  
for key, value in b:
	if value > 0:
		print("{} {}".format(key, value))
		
		
"""This code defines a dictionary "a" with keys as the capital letters of the alphabet 'A' to 'Z' and values initialized to 0. The variable "n" takes an integer input from the user, which represents the number of strings that are to be processed.

In the following for-loop with index variable "i", "n" number of strings are taken as input and split into separate words using the split() method. These words are stored in a list "m".

Another nested for-loop with index variable "j" iterates through the words in the list "m". Yet another nested for-loop with index variable "k" iterates through each character of the word at index "j". The ordinal value of the character is stored in the variable "x".

If the ordinal value of "x" is between 65 and 90 (inclusive), it is a capital letter, and its corresponding value in the dictionary "a" is incremented. If the ordinal value of "x" is between 97 and 122 (inclusive), it is a lowercase letter, and its corresponding capital letter value in the dictionary "a" is incremented by converting "x" to its capital letter counterpart using the expression "chr(x - 97 + 65)".

The dictionary "a" is then sorted in descending order based on its values using the sorted() method and the "key" parameter set to a lambda function that returns the value of an item. The sorted dictionary is stored in the list "b".

Finally, the sorted dictionary "b" is iterated over using a for-loop, and each key-value pair is printed in the format "{} {}". The key is the capital letter and the value is its frequency of occurrence in the input strings. The if statement at the end ensures that only key-value pairs with a positive value are printed.

"""


