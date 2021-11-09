def isPrime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                return False
            else:
                return True
    else:
        return False

def getGCD(x, y):
    while y != 0:
        x, y = y, x%y
    return  x

def get_RAS_PQ():
    p, q = 8, 8

    while not isPrime(p):
        p = int(input("Input a prime number for P: "))
    while not isPrime(q):
        q = int(input("Input a prime number for Q: "))

    m = input("Input a string: ")
    m_enc = []
    m_dec = []

    n = p * q
    z = (p-1)*(q-1)
    e = 0
    d = 0

    for e in range(1, n):
        if(z % e != 0):
            break

    for d in range (1, 1000):
        if(d != z and (e*d-1) != z):
            if((e*d-1) % z == 0):
                break
                
    print('----------------------------------------')
    print('-------------- ENCRYPTION --------------')
    print('----------------------------------------')
    print(f'p={p} | q={q} | n={n} | z={z} | e={e} | d={d}')

    # Assume 'A' starts at 1
    for i in range(len(m)):
        m_temp = ord(m[i])
        m_enc.append(chr((m_temp**e % n)))

    m_enc_output = ''.join(m_enc)
    print(f'Input "{m}" is encrypted to "{m_enc_output}"')

    print()
    print('----------------------------------------')
    print('-------------- DECRYPTION --------------')
    print('----------------------------------------')
    for i in range(len(m_enc_output)):
        m_temp = ord(m_enc_output[i])
        m_dec.append(chr((m_temp**d % n)))

    m_dec_output = ''.join(m_dec)
    print(f'Input "{m_enc_output}" is encrypted to "{m_dec_output}"')


def main():
    i = input(f'''
        [1] RAS Encrypt String (Inputs: P, Q, String)
        [2] RAS Encrypt String (Inputs: P, Q, E, D, String)
        ''')

if __name__ == "__main__":
    get_RAS_PQ()
    
