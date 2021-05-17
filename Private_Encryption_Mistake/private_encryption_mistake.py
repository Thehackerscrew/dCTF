from Crypto.Util.number import bytes_to_long, isPrime
from Crypto.PublicKey import RSA
from base64 import b64decode


# Partial private key received from image
upper_key = b"""
MIIJKQIBAAKCAgEAupQ7hhy0AQR0LRMZgP/Kl6J3l2+U+wp1YyVB8oDYvslE3AXU
3igwX2LOYgG/JIHQ5UI2G/0Fu5iPPikh3JoUABGFyPwWsBLnohdBBtpvfRLprhbB
lsKwjZfLJIrRex+sSFkcT9zVs1VH4JfcJAbeBNK/aQdMqc1i4JQ1xsQny4ZH7TZe
CXBigK99+V05C+ENRS1uWi9ixgcbMWCCBHsTq0Kl5FIfPvVJVBr075bf7DdARSRU
Wx/FtKVMlWe/nGUTz/ezu2jOx69kd+hvtzX1JVkeY+AFi7Ldta2tNaH/8kitzoXK
JC+6A+LQXynmjQdH9RGsg7QygFjPvIcgwE8LHsMt62OKcIx5LMHlW4lvLK/EZMnr
"""

lower_key = b"""
ZEt6WwyEqHhPyP0CggEBAMplAvElBwRTMaT6FfWwi149Q+C1+ogaRc686CkCEs7p
zWjt4+Tg3cndxj/p2Q3Z1AzJH8h/vfZruAQHF/UFwXIAPmuzS1K0HgnNHxr355vs
AYfArpTJeyZoRttQOXvRhM+c887RWGXX278VVS5e5mh16Dn0rKpDcRnsVMahBhTg
+4XheX0zJRa3lOnoWgRLFGcJj9px4Gk7PkZnx24S2bCb7GUbisvtELkLfAvVcGIS
vvJGbeovAGpArRoaCbpnRL96N50zOWGqHeXJFljvNDvfpVAbykf+50d2VApvElQ3
/v7UHVZEfszMk3g1z+RLpgVmtltCsFvDSkDW9omfoJ0CggEBAIBfu08VPrN+B8iD
QpyO2BBUDei8fjdskpvehjWGDqzKNYDxdVcAdERtk6DSWuzpvwPNbTRm6u3v66yu
QkHn9gBlxX1sYe5P9ExqP2p+Au8hR/8s7bhVa8G53WX1Dl47QVSwbKVOWSWtQSwB
hiB9s1YqgAlhcKBWP6vFbavr3VBYY5ln/018rYvR1euDVTUVZdSMmbq3gScF4fhv
NESMd1Je7XjygbVTPJPi1PcT/SgyDRUwz0RPYIvLlA3qT9ae7s5WTp1fanv5MV6p
4LnekTQ/CVjWSorY7xdXTCMfBK1GF7WhVGG4fVSPX8QeIPKUxKkQXgKAFJrCSjj7
CLG5pPkCggEAflfmKUDTC4kfkXwoXzHxHkgialFPbszvzOmyB39q3E2pU5pFTChv
"""

def get_values(priv_key):
    results = []
    data = hex(bytes_to_long(b64decode(priv_key)))
    results = data.replace('02820100', ',0x').replace('0282010100', ',0x').replace('0282020100', ',0x').split(',') # should be modified accordingly
    return results

#print ("[*] Upper key values:", get_values(upper_key))
#print ("\n")
#print ("[*] Lower key values:", get_values(lower_key))
#print ("\n")

#N_upper_bits = 0xba943b861cb40104742d131980ffca97a277976f94fb0a75632541f280d8bec944dc05d4de28305f62ce6201bf2481d0e542361bfd05bb988f3e2921dc9a14001185c8fc16b012e7a2174106da6f7d12e9ae16c196c2b08d97cb248ad17b1fac48591c4fdcd5b35547e097dc2406de04d2bf69074ca9cd62e09435c6c427cb8647ed365e09706280af7df95d390be10d452d6e5a2f62c6071b316082047b13ab42a5e4521f3ef549541af4ef96dfec37404524545b1fc5b4a54c9567bf9c6513cff7b3bb68cec7af6477e86fb735f525591e63e0058bb2ddb5adad35a1fff248adce85ca242fba03e2d05f29e68d0747f511ac83b4328058cfbc8720c04f0b1ec32deb638a708c792cc1e55b896f2cafc464c9eb
#p_lower_bits = 0x644b7a5b0c84a8784fc8fd
q = [0xca6502f12507045331a4fa15f5b08b5e3d43e0b5fa881a45cebce8290212cee9cd68ede3e4e0ddc9ddc63fe9d90dd9d40cc91fc87fbdf66bb8040717f505c172003e6bb34b52b41e09cd1f1af7e79bec0187c0ae94c97b266846db50397bd184cf9cf3ced15865d7dbbf15552e5ee66875e839f4acaa437119ec54c6a10614e0fb85e1797d332516b794e9e85a044b1467098fda71e0693b3e4667c76e12d9b09bec651b8acbed10b90b7c0bd5706212bef2466dea2f006a40ad1a1a09ba6744bf7a379d333961aa1de5c91658ef343bdfa5501bca47fee74776540a6f125437fefed41d56447ecccc937835cfe44ba60566b65b42b05bc34a40d6f6899fa09d]
#dp = 0x805fbb4f153eb37e07c883429c8ed810540de8bc7e376c929bde8635860eacca3580f175570074446d93a0d25aece9bf03cd6d3466eaedefebacae4241e7f60065c57d6c61ee4ff44c6a3f6a7e02ef2147ff2cedb8556bc1b9dd65f50e5e3b4154b06ca54e5925ad412c0186207db3562a80096170a0563fabc56dabebdd5058639967ff4d7cad8bd1d5eb8355351565d48c99bab7812705e1f86f34448c77525eed78f281b5533c93e2d4f713fd28320d1530cf444f608bcb940dea4fd69eeece564e9d5f6a7bf9315ea9e0b9de91343f0958d64a8ad8ef17574c231f04ad4617b5a15461b87d548f5fc41e20f294c4a9105e0280149ac24a38fb08b1b9a4f9
#dq_upper_bits = 0x7e57e62940d30b891f917c285f31f11e48226a514f6eccefcce9b2077f6adc4da9539a454c286f
e = 0x10001

def get_p():
    result = []
    dp = int(get_values(lower_key)[2], 16) # just comment this if you add the values inside script ^ like above
    for kp in range(1, e):
        p_mul = dp * e - 1
        if p_mul % kp == 0:
            p = (p_mul // kp) + 1
            if isPrime(p):
                result.append(p)
    return result

def get_n():
    n = [P * Q for P in get_p() for Q in q]
    return n


# Fixed reconstruct function which should be faster
def reconstruct_RSA2(pt, qt, nt):
    # Find all p * q == n combinations and make a dictionary
    combinations = {n: (x, y) for n in nt for x in pt for y in qt if n == x * y}

    if len(combinations) > 1:
        print("\n[*] Printing multiple keys\n\n")
    else:
        print("[*] Final key incoming..\n\n")
    # loop through hashmap where n = p*q combinations. n = n and p_and_q tuple where p and q
    for n, p_and_q in combinations.items():
        p, q = p_and_q[0], p_and_q[1]

        # last RSA calculations before reconstructing the private key
        phi = (p - 1) * (q - 1)
        d = pow(e, -1, phi)
        key = RSA.construct((n, e, d, p, q))
        pem = key.exportKey('PEM')
        print(pem.decode(), "\n\n\n")
        f = open('dctf_id_rsa', 'w')
        f.write(pem.decode())
        f.close

if __name__ == '__main__':
    reconstruct_RSA2(get_p(), q, get_n())
    print ("[*] Creating id_rsa...")
    import os; os.chmod('dctf_id_rsa', 0o600)
    print ("[*] Connecting to target server...")
    import paramiko
    hostname = 'dctf1-chall-private-encryption-mistake.westeurope.azurecontainer.io'
    port = 2222
    user = 'user'
    key = 'dctf_id_rsa'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=user, key_filename=key, port=port)
    shell = ssh.invoke_shell()
    print(shell.recv(8192).decode())
    print(shell.recv(8192).decode())