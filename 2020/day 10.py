with open('input10.txt') as file:
    jolts = sorted([0]+[int(jolt) for jolt in file.read().splitlines()])

d1=0
d3=1
for i in range(len(jolts)-1):
    if jolts[i+1]-jolts[i]==1:
        d1+=1
    if jolts[i+1]-jolts[i]==3:
        d3+=1
  
#soluzione 1
print(d1*d3)

connections = {node: [jolt for jolt in jolts if 1<=jolt-node<=3] for node in jolts}
all_paths = {168:1}

for node in jolts[-2::-1]:
    all_paths[node] = sum(all_paths[child] for child in connections[node])

#soluzione 2
print(all_paths[0])
