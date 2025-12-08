f = open("0042_words.txt").read()
words=[]
for word in f.split(','):
    words.append(word.strip('"'))

triangles = []
for i in range(1000):
    triangles.append(i*(i+1)//2)

count = 0
for word in words:
    num = 0
    for c in word:
        num += ord(c) - ord('A') + 1
    if num in triangles:
        count +=1
print(count)