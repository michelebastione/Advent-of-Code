import asyncio

with open('input23.txt') as file:
    data = [*map(int, file.read().split(','))]

class Executer:
    def __init__(self, array, id):
        self.array = [*array]+[0]*1000
        self.queue = [id]
        self.id = id
        self.idle = False

    async def execute(self):
        instr = self.array
        pointer = 0
        relative_base = 0
        received = False
        first_time = True
        to_send = []
        address = None

        while True:
            to_exec = instr[pointer]
            if to_exec == 99:
                break
            if len(self.queue) > 0:
                self.idle = False

            temp = str(to_exec)
            opcode =  to_exec if len(temp) < 2 else int(temp[-2:])
            parameter_1 = 0 if len(temp) < 3 else int(temp[-3])
            parameter_2 = 0 if len(temp) < 4 else int(temp[-4])
            parameter_3 = 0 if len(temp) < 5 else int(temp[-5])

            p1 = (instr[pointer+1], pointer+1, relative_base+instr[pointer+1])[parameter_1]
            if opcode == 3:
                if first_time:
                    instr[p1] = self.queue.pop()
                    first_time = False
                elif len(self.queue) == 0:
                    instr[p1] = -1
                    self.idle = True
                    pointer += 2
                    await asyncio.sleep(0)
                    continue
                elif received:
                    instr[p1] = self.queue[0][1]
                    self.queue.pop(0)
                    received = False
                else:
                    instr[p1] = self.queue[0][0]
                    received = True

                self.idle = False
                pointer += 2

            elif opcode == 4:
                if address != None:
                    to_send.append(instr[p1])
                    if len(to_send) == 2:
                        if address == 255:
                            router.last_packet = to_send
                        else:
                            executers[address].queue.append(to_send)
                            executers[address].idle = False
                        to_send = []
                        address = None
                else:
                    address = instr[p1]

                pointer += 2

            elif opcode == 9:
                relative_base += instr[p1]
                pointer += 2

            else:
                p2 = (instr[pointer+2], pointer+2, relative_base+instr[pointer+2])[parameter_2]
                if opcode == 5:
                    if instr[p1] != 0:
                        pointer = instr[p2]
                    else:
                        pointer += 3
                elif opcode == 6:
                    if instr[p1] == 0:
                        pointer = instr[p2]
                    else:
                        pointer += 3
                else:
                    p3 = (instr[pointer+3], pointer+3, relative_base+instr[pointer+3])[parameter_3]
                    if opcode == 1:
                        instr[p3] = instr[p1] + instr[p2]
                    elif opcode == 2:
                        instr[p3] = instr[p1] * instr[p2]
                    elif opcode == 7:
                        instr[p3] = 1 if instr[p1] < instr[p2] else 0
                    elif opcode == 8:
                        instr[p3] = 1 if instr[p1] == instr[p2] else 0
                    pointer += 4

            await asyncio.sleep(0)

class NAT:
    def __init__(self, net):
        self.last_packet = []
        self.net = net

    async def monitor(self):
        first_received = True
        y_sent = []

        while not self.last_packet:
            await asyncio.sleep(0)

        while True:
            if first_received:
                print(self.last_packet[1])
                first_received = False

            if all(computer.idle for computer in self.net):
                self.net[0].queue.append(self.last_packet)
                y_sent.append(self.last_packet[-1])

                #soluzione 2 estremamente lenta e probabilmente molto inefficiente, se possibile implementare un router che si occupa di gestire sul serio le connessioni
                if len(y_sent) > 1 and y_sent[-1] == y_sent[-2]:
                    print(y_sent[-1])
                    exit()
            await asyncio.sleep(0)

executers = [Executer(data, i) for i in range(50)]
router = NAT(executers)

#soluzione 1
loop = asyncio.get_event_loop()
tasks = [loop.create_task(exe.execute()) for exe in executers]
loop.run_until_complete(asyncio.gather(*(task for task in tasks), router.monitor()))
