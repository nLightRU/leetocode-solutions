n = 1000000
s = ''

pos = 1
while n != 0:
    if pos == 0:
        s = '.' + str(n % 10) + s
    else:
        s = str(n % 10) + s
    n //= 10
    pos = (pos + 1) % 3

print(s)