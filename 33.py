num = 0
denum = 0

def simplify(s1,s2):
    for c in s1:
        if c in s2:
            s2.remove(c)
            s1.remove(c)
            return True
    return False

for denum in range(10,100):
    for num in range(10,denum):
        if num%10==0 or denum%10==0:
            continue
        snum = list(str(num))
        sdenum = list(str(denum))
        if not simplify(snum,sdenum):
            continue
        
        if int(''.join(snum))/int(''.join(sdenum)) == num/denum:
            print(num,denum)
        