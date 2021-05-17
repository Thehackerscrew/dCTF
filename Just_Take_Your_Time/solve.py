from pwn import *
from Crypto.Cipher import DES3
from time import time


p = remote('dctf-chall-just-take-your-time.westeurope.azurecontainer.io', 9999)
p.recvline()
tmp = p.recvline().strip().decode()
info(tmp)
tmp = tmp.split(' ')
res = int(tmp[0])*int(tmp[2])
success(str(res))
p.sendlineafter("> ",str(res))
t = int(time())
p.recvline()
encrypted = str(p.recvline().decode())
info(encrypted)
key = str(t-1).zfill(16).encode()
cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
FUZZ = bytes.fromhex(encrypted)
decrypted = cipher.decrypt(FUZZ)
success(decrypted)
p.sendlineafter("> ", decrypted)
opt = p.recv(1024)
print(opt.decode())