with open('input8.txt') as file:
    strings = file.read().splitlines()

#soluzione 1
print(sum(len(string)-len(eval(string)) for string in strings))

#soluzione 2
print(sum(len(repr(string))+string.count("\"")-len(string) for string in strings))
