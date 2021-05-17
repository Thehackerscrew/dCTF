from socket import socket
from sage.all import *

class lsfr:
    def __init__(self, state, coefs):
        self.state = state
        self.coefs = coefs

    def next(self):
        n = sum([self.state[i] * self.coefs[i] for i in range(10)]) % 5039
        self.state = self.state[1:] + [n]
        return n

def check(pin, guess):
    a,b = 0,0
    for i in range(len(guess)):
        if guess[i] in pin:
            if pin.index(guess[i]) == i: a += 1
            else: b += 1
    return f"A{a}B{b}"

def unique(n):
    return len(set("%04d" % n)) == 4

initguess = "1234"+''.join(str(i)*(2**i) for i in range(10))
allpins = ["%04d" % n for n in range(10000) if unique(n)]
N = 200
info = []

s = socket()
s.connect(("dctf1-chall-lockpicking.westeurope.azurecontainer.io", 7777))
print(s.recv(8192))

for _ in range(20):
    s.sendall((initguess+"\n").encode())
    resp = s.recv(8192).decode().splitlines()[0].split(" ")[2]
    cands = cands = [e for e in allpins if check(e, initguess)==resp]

    while True:
        guess = cands.pop(0)
        s.sendall((guess+"\n").encode())
        print(f"Guessing {guess}")
        resp = s.recv(8192)
        if b"Correct" in resp:
            info.append(allpins.index(guess))
            break
        else:
            resp = resp.decode().splitlines()[0].split(" ")[2]
            cands = [e for e in cands if check(e, guess)==resp]

A = matrix(GF(5039), ncols=10, nrows=10)
b = vector(GF(5039), info[10:20])
for i in range(10):
    A[i] = info[i:i+10]

new_rng = lsfr(info[10:20], list(A.solve_right(b)))

pins = [allpins[new_rng.next()] for _ in range(N-20)]

for pin in pins:
    print("Pin: ",pin)
    s.sendall((pin+"\n").encode())
    resp = s.recv(8192)
    print(resp.decode())
    if b"Congrat" in resp:
        break
        #input("???")
