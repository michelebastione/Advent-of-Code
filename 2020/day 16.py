from my_funcs import prod

with open('input16.txt') as file:
    data = file.read().split('\n\n')

temp1 = [temp.split(': ') for temp in data[0].splitlines()] 
temp2 = [temp[1].split(' or ') for temp in temp1]
temp3 = [[range(int(i.split('-')[0]),int(i.split('-')[1])+1) for i in temp] for temp in temp2]

fields = {temp1[i][0]: [*temp3[i][0]]+[*temp3[i][1]] for i in range(len(temp3))}
nearby = data[2].split('nearby tickets:\n')[1].splitlines()
tickets = [[int(k) for k in line.split(',')] for line in nearby]
tickets_loose = [int(k) for line in nearby for k in line.split(',')]

#soluzione 1
print(sum(n for n in tickets_loose if all(n not in field for field in fields.values())))

valids = []
for ticket in tickets:
   if all(any(t in field for field in fields.values()) for t in ticket):
       valids.append(ticket)

order = {field:[] for field in fields}
for field in fields:
    for i in range(20):
        if all(valid[i] in fields[field] for valid in valids):
            order[field].append(i)

ones = []
while any(len(order[i])!=1 for i in order):
    for j in order:
        if len(order[j])==1:
            oj = order[j][0]
            if oj in ones:
                continue
            ones.append(oj)
            for k in order:
               if len(order[k])==1:
                   continue
               if oj in order[k]:
                   order[k].remove(oj)

order = {value: order[value][0] for value in order}
my_ticket = [int(x) for x in data[1].split('your ticket:\n')[1].split(',')]

#soluzione 2
print(prod([my_ticket[order[field]] for field in fields if 'departure' in field]))
