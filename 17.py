import num2words

def sLen(s):
    sum = 0
    for c in s:
        if c=='-' or c==' ':
            continue
        sum+=1
    return sum

s = num2words.num2words(342)
print(s,sLen(s))

s = num2words.num2words(115)
print(s,sLen(s))

sum = 0
for i in range(1,1001):
    s = num2words.num2words(i)
    sum += sLen(s)
print(sum)