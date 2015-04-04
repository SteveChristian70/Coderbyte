'''
Have the function LongestWord(sen) take the sen parameter being passed and return
the largest word in the string. If there are two or more words that are the same
length, return the first word from the string with that length. 
Ignore punctuation and assume sen will not be empty. 
'''

symbols = ('!','@','#','$','%','^','&','*','(',')')

def LongestWord(sen): 

  sen = ''.join([char for char in sen if char not in symbols])
  res = sen.split()
  max = 0
  for word in res:
  	if (len(word) > max):
  		max = len(word)
  		res = word
  return res
    
    
print LongestWord(raw_input()) 