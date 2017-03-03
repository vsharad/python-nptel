def orangecap(input):
  players = dict()
  match = dict()
  score = -1
  for key_match in input:
    match = input[key_match]
    for key_player in match:
      if key_player in players:
        current = players[key_player]
        players[key_player] = current + input[key_match][key_player]
      else:
        players[key_player] = input[key_match][key_player]
  orange_cap_player = max(players,key=players.get)
  return(orange_cap_player,players[orange_cap_player])
  
def addpoly(p1,p2):
  poly1 = dict()
  poly2 = dict()
  addition = dict()
  poly1 = {list[1]:list[0] for list in p1}
  #print(poly1)
  poly2 = {list[1]:list[0] for list in p2}
  #print(poly2)
  for key_p1 in poly1:
    addition[key_p1] = poly1[key_p1]
    if key_p1 in poly2:
      addition[key_p1] += poly2[key_p1]  
  for key_p2 in poly2:
    if key_p2 not in poly1:
      addition[key_p2] = poly2[key_p2]
  #print(addition)
  list = [(v,k) for k,v in addition.items() if v != 0]
  #print(list)
  list.sort(key = lambda tup: tup[1],reverse=True)
  return(list)
  
def multpoly(p1,p2):
  poly1 = dict()
  poly2 = dict()
  multiply = dict()
  poly1 = {list[1]:list[0] for list in p1}
  #print(poly1)
  poly2 = {list[1]:list[0] for list in p2}
  #print(poly2)
  for key_p1 in poly1:
    for key_p2 in poly2:
      temp = key_p1 + key_p2
      if temp in multiply:
        multiply[temp] += poly1[key_p1] * poly2[key_p2]
      else:
        multiply[temp] = poly1[key_p1] * poly2[key_p2]
  list = [(v,k) for k,v in multiply.items() if v != 0]
  #print(list)
  list.sort(key = lambda tup: tup[1],reverse=True)
  return(list)