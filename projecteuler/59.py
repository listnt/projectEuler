import itertools

f = open("0059_cipher.txt").read()

f = f.split(",")
cipher = [int(x) for x in f]

key = [0,0,0]
for i in range(ord('a'),ord('z')+1):
    for j in range(ord('a'),ord('z')+1):
        for k in range(ord('a'),ord('z')+1):
            key = [i,j,k]
            plain = [chr(x^y) for x,y in zip(cipher,itertools.cycle(key))]
            if "the" in ''.join(plain):
                # through experint I found that the key is exp
                # print(''.join([chr(c) for c in key]),''.join(plain))
                break
            
key = [ord('e'),ord('x'),ord('p')]

plain = [chr(x^y) for x,y in zip(cipher,itertools.cycle(key))]
print(sum([ord(x) for x in plain]))