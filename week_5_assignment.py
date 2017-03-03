match = "Djokovic:Murray:2-6,6-7,7-6,6-3,6-1"
temp = match
winner = temp[:temp.find(":")]
temp = temp[temp.find(":")+1:]
loser = temp[:temp.find(":")]
score = temp[temp.find(":")+1:]
set = [set.split("-") for set in score.split(",")]
players = dict()
players[winner] = {'5m':0,'3m':0,'sw':0,'gw':0,'sl':0,'gl':0}
players[loser] = {'5m':0,'3m':0,'sw':0,'gw':0,'sl':0,'gl':0}
if len(set)>3:
  players[winner]['5m']+=1
else:
  players[winner]['3m']+=1

for s in set:
  sw,sl,gw,gl = 0
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
  