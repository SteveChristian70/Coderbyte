'''Have the function SimpleAdding(num) add up all the numbers from 1 to num.
For the test cases, the parameter num will be any number from 1 to 1000. 

Use the Parameter Testing feature in the box below
to test your code with different arguments.'''

def SimpleAdding(num): 

  sum = 0
  for i in range(0, num):
    sum += i
  return sum + num
    
print SimpleAdding(raw_input())
