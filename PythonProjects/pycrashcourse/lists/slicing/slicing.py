players = ['charles', 'martin','michel', 'florence', 'elite']
print(players)
# indexing
print(players[0])
print(players[1])
print(players[2])
print(players[3])
print(players[4])
# REVERSE INDEXING
print(players[-1])
print(players[-2])
print(players[-3])
print(players[-4])
print(players[-5])
# slicing
# slicing first three elements
print(players[0:3])
print(players[0:4])
print(players[1:4])
print(players[:4])
print(players[4:])
print(players[2:])
print(players[-3:])

for player in players[:3]:
    print(player)
for player in players[3:]:
    print(player)