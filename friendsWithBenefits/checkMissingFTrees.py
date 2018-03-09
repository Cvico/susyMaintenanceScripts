import os, sys

# this script can be used to verify that a folder contains a Friend Tree for each of the friend trees in other one, aka, you produced everything

completeDir = sys.argv[1]
newDir = sys.argv[2]

inSets = [d.replace('evVarFriend_','').replace('.root','') for d in os.listdir(completeDir) if ('evVarFriend' in d and 'chunk' not in d)]
outSets = [d.replace('evVarFriend_','').replace('.root','') for d in os.listdir(newDir) if ('evVarFriend' in d and 'chunk' not in d)]

missingSets = []

for d in inSets:
  if d in outSets: continue
  else: print "Friend tree: %s missing"%d
  missingSets.append(d)

print "_________________ %i friend trees are missing __________________"%len(missingSets)
print missingSets
