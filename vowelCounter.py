'''
Have the function VowelCount(str) take the str string parameter 
being passed and return the number of vowels the string contains 
(ie. "All cows eat grass" would return 5). Do not count y as a vowel for this challenge. 

Use the Parameter Testing feature in the box below to test
 your code with different arguments.
 '''


def VowelCount(str): 

  count = 0
  for x in str:
    if x in "aeiou":
      count += 1
  return count
    
print VowelCount(raw_input())           
