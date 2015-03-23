'''
Have the function ExOh(str) take the str parameter being passed and return
the string true if there is an equal number of x's and o's, otherwise return 
the string false. Only these two letters will be entered in the string, 
no punctuation or numbers. For example: if str is "xooxxxxooxo" then the 
output should return false because there are 6 x's and 5 o's.
'''



def charCount(word, char):

	count = 0
	for i in word:
		if i == char:
			count += 1
	return count
	
def ExOh(str):

	o = charCount(str, 'o')
	x = charCount(str, 'x')
	if x == o:
		return 'true'
	return 'false'
	


# Alternate way to solve problem

def ExOh(str):
	x = 0
	o = 0
	for char in str:
		if char == 'x':
			x += 1
		elif char == 'o':
			o += 1
	return 'true' if x == o else 'false'