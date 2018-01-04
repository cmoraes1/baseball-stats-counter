import re
import sys, os

if len(sys.argv) < 2:
    sys.exit("Usage: python3 %s filename" %sys.argv[0])

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit("Error: File '%s' not found" % sys.argv[1])
 
f = open(filename, "r")
player_info = {}
pattern = re.compile("((?P<name>^[a-zA-Z]{2,}\s[a-zA-z]{1,})\sbatted\s(?P<atBats>\d)\stimes\swith\s(?P<hits>\d)\shits\sand\s(?P<runs>\d)\sruns)")
for line in f:  
    find_match = re.match(pattern, line)

    if find_match:
        name = find_match.group('name')
        atBats = int(find_match.group('atBats'))
        hits = int(find_match.group('hits'))
        
        if name is None:
            continue
        else: 
            if not name in player_info:
                player_info[name] = {
                    'atBats': atBats,
                    'hits': hits
                }   
            else:
                player_info[name]['atBats'] += atBats
                player_info[name]['hits'] += hits
    else:
        continue 
    
final_stats = []
for player in player_info:
    battingAverage = float(player_info[player]['hits'])/float(player_info[player]['atBats'])
    final_stats.append((player, battingAverage))

sorted_players = sorted(final_stats, reverse=True, key=lambda player:player[1])    
for player in sorted_players:
    print(player[0] + ":",  "%.3f" %  player[1])   
