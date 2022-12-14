
with open('input5.txt')as file:
    bpss = file.read().splitlines()

row = lambda y: int(''.join(map(lambda x:'0' if x=='F' else '1', y)), 2)
column = lambda y: int(''.join(map(lambda x:'0' if x=='L' else '1', y)), 2)
bpid = lambda x: row(x[:7])*8+column(x[7:])

all_bpid = [*map(bpid, bpss)]
#soluszione 1
print(max(all_bpid))

for i in range(all_bpid[0], all_bpid[-1]):
    if i not in sorted(all_bpid):
        #soluzione 2
        print(i)
