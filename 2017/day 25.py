import numpy as np
import asyncio

class Tape:
    def __init__(self, steps):
        self.steps = steps
        self.count = 0
        self.array = np.zeros(10**5, dtype = int)
        self.pointer = 50000
        self.semaforo = dict(zip('ABCDEF', [True]+[False]*5))

    async def A(self):
        while True:
            while not self.semaforo['A']:
                if self.count == self.steps:
                    break
                await asyncio.sleep(0)
            if self.count == self.steps:
                break
            self.count += 1
            if self.array[self.pointer]:
                self.array[self.pointer] = 0
                self.pointer -= 1
                self.semaforo['A'] = False
                self.semaforo['C'] = True
                await asyncio.sleep(0)
            else:
               self.array[self.pointer] = 1
               self.pointer += 1
               self.semaforo['A'] = False
               self.semaforo['B'] = True
               await asyncio.sleep(0)

    async def B(self):
        while True:
            while not self.semaforo['B']:
                if self.count == self.steps:
                    break
                await asyncio.sleep(0)
            if self.count == self.steps:
                break
            self.count += 1
            if self.array[self.pointer]:
                self.pointer -= 1
                self.semaforo['B'] = False
                self.semaforo['D'] = True
                await asyncio.sleep(0)
            else:
                self.array[self.pointer] = 1
                self.pointer -= 1
                self.semaforo['B'] = False
                self.semaforo['A'] = True
                await asyncio.sleep(0)

    async def C(self):
        while True:
            while not self.semaforo['C']:
                if self.count == self.steps:
                    break
                await asyncio.sleep(0)
            if self.count == self.steps:
                break
            self.count += 1
            if self.array[self.pointer]:
                self.array[self.pointer] = 0
                self.pointer += 1
            else:
                self.array[self.pointer] = 1
                self.pointer += 1
                self.semaforo['C'] = False
                self.semaforo['D'] = True
                await asyncio.sleep(0)

    async def D(self):
        while True:
            while not self.semaforo['D']:
                if self.count == self.steps:
                    break
                await asyncio.sleep(0)
            if self.count == self.steps:
                break
            self.count += 1
            if self.array[self.pointer]:
                self.array[self.pointer] = 0
                self.pointer += 1
                self.semaforo['D'] = False
                self.semaforo['E'] = True
                await asyncio.sleep(0)
            else:
                self.pointer -= 1
                self.semaforo['D'] = False
                self.semaforo['B'] = True
                await asyncio.sleep(0)

    async def E(self):
        while True:
            while not self.semaforo['E']:
                if self.count == self.steps:
                    break
                await asyncio.sleep(0)
            if self.count == self.steps:
                break
            self.count += 1
            if self.array[self.pointer]:
                self.pointer -= 1
                self.semaforo['E'] = False
                self.semaforo['F'] = True
                await asyncio.sleep(0)
            else:
                self.array[self.pointer] = 1
                self.pointer += 1
                self.semaforo['E'] = False
                self.semaforo['C'] = True
                await asyncio.sleep(0)

    async def F(self):
        while self.count < self.steps:
            while not self.semaforo['F']:
                if self.count == self.steps:
                    break
                await asyncio.sleep(0)
            if self.count == self.steps:
                break
            self.count += 1
            if self.array[self.pointer]:
                self.pointer += 1
                self.semaforo['F'] = False
                self.semaforo['A'] = True
                await asyncio.sleep(0)
            else:
                self.array[self.pointer] = 1
                self.pointer -= 1
                self.semaforo['F'] = False
                self.semaforo['E'] = True
                await asyncio.sleep(0)

#soluzione 1 (estremamente inefficiente ma non ho voglia di ottimizzarla)
garbage_collector = Tape(12172063)
loop = asyncio.get_event_loop()
ta = loop.create_task(garbage_collector.A())
tb = loop.create_task(garbage_collector.B())
tc = loop.create_task(garbage_collector.C())
td = loop.create_task(garbage_collector.D())
te = loop.create_task(garbage_collector.E())
tf = loop.create_task(garbage_collector.F())
loop.run_until_complete(asyncio.gather(ta, tb, tc, td, te, tf))
print(np.count_nonzero(garbage_collector.array))