def statistics(input):
  players = dict()
  for match in input:
    #match = "Djokovic:Murray:2-6,6-7,7-6,6-3,6-1"
    temp = match
    winner = temp[:temp.find(":")]
    temp = temp[temp.find(":")+1:]
    loser = temp[:temp.find(":")]
    score = temp[temp.find(":")+1:]
    #set = [set.split("-") for set in score.split(",")]
    #set = [[int(game[0]),int(game[1])] for game in set]
    set = [[int(game[0]),int(game[1])] for set in score.split(",") for game in [set.split("-")]]
    if winner not in players:
      players[winner] = {'5m':0,'3m':0,'sw':0,'gw':0,'sl':0,'gl':0}
    if loser not in players:
      players[loser] = {'5m':0,'3m':0,'sw':0,'gw':0,'sl':0,'gl':0}
    if len(set)>3:
      players[winner]['5m']+=1
    else:
      players[winner]['3m']+=1
    sw,sl,gw,gl = 0,0,0,0
    for s in set:
      if s[0] > s[1]:
        sw += 1
      else:
        sl +=1
      gw += s[0]
      gl += s[1]
    
    players[winner]['sw'] += sw
    players[winner]['sl'] += sl
    players[winner]['gw'] += gw
    players[winner]['gl'] += gl
    
    players[loser]['sw'] += sl
    players[loser]['sl'] += sw
    players[loser]['gw'] += gl
    players[loser]['gl'] += gw
  return players

def get_input():
  lines=[]
  while True:
    line = input()
    if line:
      lines.append(line)
    else:
      break
  return lines

def sort(unsorted):
  order = sorted(unsorted.items(),key=lambda x:(-x[1]['5m'],-x[1]['3m'],-x[1]['sw'],-x[1]['gw'],x[1]['sl'],x[1]['gl']))
  for player in order:
    print("{0} {1} {2} {3} {4} {5} {6}".format(player[0],player[1]['5m'],player[1]['3m'],player[1]['sw'],player[1]['gw'],player[1]['sl'],player[1]['gl']))

input = get_input()
stats = statistics(input)
test = sort(stats)