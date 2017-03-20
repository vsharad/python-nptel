'''
Question 1

Here is an function to return the maximum value among three positive integers. There is an error in this function. Provide an input triple (n1,n2,n3), where n1, n2 and n3 are all positive integers, for which max3bad produces an incorrect output.

def max3bad(x,y,z):
  maximum = 0
  if x >= y:
    if x >= z:
      maximum = x
  elif y >= z:
    maximum = y
  else:
    maximum = z
  return(maximum)
Open up the code submission box below and write your test case where you would normally paste your code, below the line myinput = ' ''. Your input should be in the form of triple (n1,n2,n3), where n1, n2 and n3 are all positive integers.
'''
(2,1,3)

'''
Question 2

Here is an implementation of mergesort, along with the associated merge function. There is a small error in the implementation. Provide an input list for which this version of mergesort produces an incorrect output.

def mergebad(l1,l2):

  (lmerged,i,j) = ([],0,0)

  while i+j < len(l1) + len(l2):
    if i == len(l1):
      lmerged.append(l2[j])
      j = j+1
    elif j == len(l2):
      lmerged.append(l1[i])
      i = i+1
    elif l1[i] < l2[j]:
      lmerged.append(l1[i])
      i = i+1
    elif l2[j] < l1[i]:
      lmerged.append(l2[j])
      j = j+1
    else:
      lmerged.append(l1[i])
      i = i+1
      j = j+1
    
  return(lmerged)    

def mergesortbad(l):
  if len(l) < 2:
    return(l)
  else:
    n = len(l)
    leftsorted = mergesortbad(l[:n//2])
    rightsorted = mergesortbad(l[n//2:])
    return(mergebad(leftsorted,rightsorted))
Open up the code submission box below and write your test case where you would normally paste your code, below the line myinput = ' ''
'''
[2,2,1]

'''
Question 3

Here is a function to compute the second largest value in a list of distinct positive integers. You have to fill in the missing lines. You can assume that there are at least two numbers in the list.

def secondmax(l):
  (mymax,mysecondmax) = (0,0)
  for i in range(len(l)):
  # Your code below this line


  # Your code above this line
  return(mysecondmax)
Open up the code submission box below and fill in the gap in the code. Ensure that you maintain correct indentation.
'''
def secondmax(l):
  (mymax,mysecondmax) = (0,0)
  for i in range(len(l)):
  # Your code below this line
    if l[i] > mysecondmax:
      if l[i] > mymax:
        (mymax,mysecondmax) = (l[i],mymax)
      else:
        mysecondmax = l[i]
  # Your code above this line
  return(mysecondmax)

'''
Question 4

A list is a palindrome if it reads the same forwards and backwards. For instance [], [7], [8,11,8] and [19,3,44,44,3,19] are palindromes, while [3,18,4] and [23,14,3,14,3,23] are not. Here is a recursive function to check if a list is a palindrome. You have to fill in the missing argument for the recursive call.

def mypalindrome(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(...)
Open up the code submission box below and fill in the missing argument for the recursive call.
'''
def mypalindrome(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(
       # Complete the recursive call below this line
mypalindrome(l[1:len(l)-1]) if(l[0] == l[len(l)-1]) else False
       # Complete the recursive call above this line
    )

'''
Question 5

A positive integer n is said to be perfect if the sum of the factors of n, other than n itself, add up to n. For instance 6 is perfect since the factors of 6 are {1,2,3,6} and 1+2+3=6. Likewise, 28 is perfect because the factors of 28 are {1,2,4,7,14,28} and 1+2+4+7+14=28.

Write a Python function perfect(n) that takes a positive integer argument and returns True if the integer is perfect, and False otherwise.
'''
def perfect(n):
  sum = 0
  for i in range(1, n):
      if n % i == 0:
        sum = sum + i
  if(sum == n):
    return True
  else:
    return False

'''
Question 6

Write a Python function sublist(l1,l2) that takes two sorted lists as arguments and returns True if the the first list is a sublist of the second list, and returns False otherwise.

A sublist of a list is a segment consisting of contiguous values, without a gap. Thus, [2,3,4] is a sublist of [2,2,3,4,5], but [2,2,4] and [2,4,5] are not.
'''
def sublist(a,b):
  l1, l2 = len(a), len(b)
  for i in range(l2):
      if a == b[i:i+l1]:
          return True
  return False

'''
Question 7

Write a Python program that reads input from the keyboard (standard input). The input will consist of some number of lines of text. The input will be terminated by a blank line. Your program should print every third line.

For instance, if the input is the following:

"Spot the mistake
in the following argument",
Jack challenged
1+(-1+1)+(-1+1)+... = (1+ -1)+(1+ -1)+...
so therefore,
1 = 0
??

then the output should be:

Jack challenged
1 = 0
'''
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        if (len(lines) > 2):
          for i in range(2,len(lines),3):
            print(lines[i])
        break


'''
Question 8

Write a Python function repeated(l) that takes a list of immutable values as argument. The function should return the number of values that are repeated in the input list.

For instance, repeated([1,17,22,17,23,17]) should return 1 because only 1 value, 17 is repeated. Likewise repeated(["the","higher","you","climb","the","further","you","fall"]) is 2 becaues 2 values, "the" and "you", are repeated.

'''
def repeated(l):
  words = dict()
  for i in l:
    if i in words.keys():
      words[i] = words[i] + 1
    else:
      words[i] = 1
  repeat_words = [key for key,value in words.items() if value > 1]
  return len(repeat_words)
