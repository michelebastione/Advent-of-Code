with open('input16.txt') as file:
    data = ''
    for bit in file.read():
        b = bin(int(bit, 16))[2:]
        data += f"{'0'*(4-len(b))}{b}"

class Packet:
    def __init__(self, version, type):
        self.version = version
        self.type = type

# soluzione 1
packets = []
def decode(code, countdown=0):
    pointer = 0
    count = 0
    while pointer < len(code):
        if all(i == '0' for i in code[pointer:]):
            break
        current_ver = int(code[pointer: pointer+3], 2)
        current_type = int(code[pointer+3: pointer+6], 2)
        new_packet = Packet(current_ver, current_type)
        pointer += 6
        number = ''
        if current_type == 4:
            while True:
                number += code[pointer+1: pointer+5]
                pointer += 5
                if code[pointer-5] == '0':
                    new_packet.number = int(number, 2)
                    break
        else:
            if code[pointer] == '0':
                length = int(code[pointer+1: pointer+16], 2)
                pointer += 16
                decode(code[pointer: pointer+length])
                pointer += length
            else:
                n_sub_packets = int(code[pointer+1: pointer+12], 2)
                pointer += 12
                pointer += decode(code[pointer:], n_sub_packets)
        count += 1
        packets.append(new_packet)
        if countdown and count == countdown:
            return pointer

decode(data)
print(sum(packet.version for packet in packets))
