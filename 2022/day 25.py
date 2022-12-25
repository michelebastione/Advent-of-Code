with open("input25.txt") as file:
    data = file.read().splitlines()


def read_snafu(n):
    num = 0
    for i, j in enumerate(n[::-1]):
        if j == "-":
            num -= 5**i
        elif j == "=":
            num -= 2*5**i
        else:
            num += int(j)*5**i
    return num


def make_snafu(n):
    raw = ""
    exp = 0
    while 5**(exp + 1) < n:
        exp += 1
    for i in range(exp, -1, -1):
        m, n = divmod(n, 5**i)
        raw += str(m)
    dig = map(int, raw)
    result = ""
    carry = 0
    for j in [*dig][::-1]:
        temp = j + carry
        carry = 1
        if temp == 3:
            result += "="
        elif temp == 4:
            result += "-"
        elif temp == 5:
            result += "0"
        else:
            result += str(temp)
            carry = 0
    if carry:
        result += "1"
    return result[::-1]


# solution
total = sum(read_snafu(i) for i in data)
print(make_snafu(total))
