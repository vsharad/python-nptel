data = list()

def Best(i):
  if i == 0:
    return 1
  else:
    max_length = 1
    for j in range(0,i):
      if(data[i] % data[j] == 0):
        max_length = max(max_length,Best(j)+1)
  return max_length

def dividing_sub(data):
  all_dividing_subsequence = [Best(i) for i in range(0,len(data))]
  return max(all_dividing_subsequence)

def read_lines():
  number_of_lines = int(input())
  while number_of_lines > 0:
    number_of_lines -= 1
    data.append(int(input()))
  answer = dividing_sub(data)
  return answer

read_lines()
9
2
3
7
8
14
39
145
76
320



