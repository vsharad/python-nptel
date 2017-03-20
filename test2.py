'''
Question 1

Here is a function isprimebad that takes a positive integer as input and returns True if the number is prime and False otherwise. There is an error in this function. Provide an input n, which is a positive integer, for which isprimebad produces an incorrect output.

import math

def isprimebad(n):
  if n < 2:
    return(False)
  else:
    for i in range(2, int(math.sqrt(n))):
      if n%i == 0:
         return(False)
    return(True)
Open up the code submission box below and write your test case where you would normally paste your code, below the line myinput = ' ''. Your input should be a single integer n.
'''
6

'''
Question 2

Here is a function lexsortbad that takes a list of pairs of integers as input and returns them in lexicographically sorted order (i.e., dictionary order). There is an error is this function. Provide an input for which lexsortbad produces an incorrect output. Your input should be a list of pairs of integers of the form [(i1,j1),(i2,j2),...,(in,jn)].

def lexsortbad(l):
  for k in range(2):
    for j in range(len(l)-1):
      for i in range(len(l)-1):
        if l[i][k] > l[i+1][k]:
          (l[i],l[i+1]) = (l[i+1],l[i])
  return(l)
Open up the code submission box below and write your test case where you would normally paste your code, below the line myinput = ' ''. Your input should be a list of pairs of integers of the form [(i1,j1),(i2,j2),...,(in,jn)].
'''
[(1,4),(3,6),(2,8)]

'''
Question 3

Here is a function to compute the largest of four input integers. You have to fill in the missing lines.

def max4(w,x,y,z):
  if w >= x and w >= y and w >= z:
    maximum = w
  # Your code below this line


  # Your code above this line
  return(maximum)
Open up the code submission box below and fill in the gap in the code. Ensure that you maintain correct indentation.
'''
def max4(w,x,y,z):
  if w >= x and w >= y and w >= z:
    maximum = w
  # Your code below this line
  elif x >= w and x >= y and x >= z:
    maximum = x
  elif y >= w and y >= x and y >= z:
    maximum = y
  else:
    maximum = z
  # Your code above this line
  return(maximum)

'''
Question 4

A list is a non-decreasing if each element is at least as big as the preceding one. For instance [], [7], [8,8,11] and [3,19,44,44,63,89] are non-decreasing, while [3,18,4] and [23,14,3,14,3,23] are not. Here is a recursive function to check if a list is non-decreasing. You have to fill in the missing argument for the recursive call.

def nondecreasing(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(...)
Open up the code submission box below and fill in the missing argument for the recursive call.
'''
def nondecreasing(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(
nondecreasing(l[1:]) if (l[0]<=l[1]) else False
       # Complete the recursive call above this line
    )

'''
Question 5

A positive integer n is a sum of squares if n = i2 + j2 for integers i,j such that i ≥ 1 and j ≥ 1. For instance, 10 is a sum of squares because 10 = 12 + 32, and so is 25 (32 + 42). On the other hand, 11 and 3 are not sums of squares.
Write a Python function sumofsquares(n) that takes a positive integer argument and returns True if the integer is a sum of squares, and False otherwise.
'''
import math
def sumofsquares(n):
  for i in range(1,math.ceil(math.sqrt(n))):
    for j in range(1,math.ceil(math.sqrt(n))):
      if n == i*i + j*j:
        return (True)
  return (False)

'''
Question 6

Write a Python function subsequence(l1,l2) that takes two sorted lists as arguments and returns True if the the first list is a subsequence of the second list, and returns False otherwise.

A subsequence of a list is obtained by dropping some values. Thus, [2,3,4] and [2,2,5] are subsequences of [2,2,3,4,5], but [2,4,4] and [2,4,3] are not.
'''
def subsequence(l1,l2):
    it = iter(l2)
    return all(any(l2elem == l1elem for l2elem in it) for l1elem in l1)

'''
Question 7

Write a Python program that reads input from the keyboard (standard input). The input will consist of some number of lines of text. The input will be terminated by a blank line. The first line will consist of a single word to be interpreted as a pattern, after discarding the new line character. Your program should print every line from the second line onward that contains an occurrence of the pattern. You can assume that the input will have a non-empty pattern line. Recall that for a string s and a pattern p, s.find(p) returns the first position in s where p occurs, and returns -1 if p does not occur in s.

For instance, if the input is the following:

the
"Spot the mistake
in the following argument",
Jack challenged
1+(-1+1)+(-1+1)+... = (1+ -1)+(1+ -1)+...
so therefore,
1 = 0
??

then your program should print the following. Note that the pattern string the is matched by the word therefore.

"Spot the mistake
in the following argument",
so therefore,
'''
lines = []
while True:
  line = input()
  if line:
    lines.append(line)
  else:
    first = lines[0]
    for i in range(1,len(lines)-1):
      if(lines[i].find(first) > -1):
        print(lines[i])
    break

'''
Question 8

Write a Python function maxaggregate(l) that takes a list of pairs of the form (name,score) as argument, where name is a string and score is an integer. Each pair is to be interpreted as the score of the named player. For instance, an input of the form [('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)] represents two scores of 73 and 7 for Kohli, two scores of 33 and 90 for Ashwin and one score of 122 for Pujara. Your function should compute the players who have the highest aggregate score (aggegrate = total, so add up all scores for that name) and return the list of names of these players as a list, sorted in alphabetical order. If there is a single player, the list will contain a single name.

For instance, maxaggregate([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)]) should return ['Ashwin'] because the aggregate score of Kolhi is 80, of Ashwin is 123 and of Pujara is 122, of which 123 is the highest.
'''
def maxaggregate(l):
  scores = dict()
  for name,score in l:
    if name in scores.keys():
      scores[name] += score
    else:
      scores[name] = score
  max_score = max(scores.values())
  max_scorers = [name for name,score in scores.items() if score == max_score]
  max_scorers.sort()
  return max_scorers

maxaggregate([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',22),('Ashwin',47)])

















