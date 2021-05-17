from pwn import *
from string import ascii_letters, digits
from math import ceil, log

alp = ascii_letters + digits + "_!@#$%.'\"+:;<=}{"

sb = {}

fl = 42
r = int(2 * ceil(log(fl, 2)))

p = remote('dctf1-chall-sp-box.westeurope.azurecontainer.io', 8888)
p.recvline()
ct = p.recvline().strip().decode()
info(ct)

for i in range(len(alp)):
    p.sendlineafter('> ', alp[i] * fl)
    p.recvline()
    sb[p.recvline().decode()[0]] = alp[i]

print(sb)

flag = ''
for c in ct:
    flag += sb[c]

info(flag)

def un_shuffle(m):
    global fl
    res = [''] * fl
    s1 = m[:fl // 2]
    s2 = m[fl // 2:]

    i = 0
    x = 0
    y = 0
    while i < fl:
        if i % 2 == 1:
            res[i] = s1[x]
            x += 1
        else:
            res[i] = s2[y]
            y += 1
        i += 1
    return ''.join(res)

for _ in range(r-1):
    flag = un_shuffle(flag)

success(flag)
p.sendlineafter('> ',flag)
opt = p.recv(1024)
print (opt.decode())