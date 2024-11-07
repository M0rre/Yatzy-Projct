from collections import Counter
final_outcome = [4,6,6,4,4,]
c = Counter(final_outcome)
# Two pairs
nice_list = []
another_list = []
nice_list = [n for n in sorted(((u for u,j in c.items() if j >= 2)),reverse=True)]
for i in range(2):
    another_list.append(nice_list[i])
print(another_list)
print(sum(another_list)*2)
nice_list=[]

# Two pairs but better
print(sum(n for n in sorted((u for u,j in c.items() if j >= 2),reverse=True)[:2])*2)

# Full house
full_house_identified = True

if full_house_identified == True and len(c) == 2 and any(u for u,j in c.items() if j == 2) and any(u for u,j in c.items() if j == 3):
    print("done")
    
full_house = sum(n for n in list(sorted((u for u,j in c.items() if j >= 2),reverse=True)))*2
print(full_house)
#^^ Just excessive simply sum() smh
print(len(c))