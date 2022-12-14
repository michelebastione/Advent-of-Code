from math import log

elfs = 3014387

first_elf = 1
final_elf = elfs

#soluzione 1
skip_step = 2
while first_elf != final_elf:
    temp_elf = final_elf
    while (temp_elf-first_elf) % skip_step != 0:
        temp_elf -= skip_step//2
    first_elf += skip_step if temp_elf == final_elf else 0
    final_elf = temp_elf
    skip_step *= 2
print(final_elf)

#soluzione 2 (ho dedotto un pattern dal plot dei primi 1000 "cerchi")
exp = int(log(elfs, 3))
r = elfs % 3**exp
print(r if r < elfs//2 else r+1)