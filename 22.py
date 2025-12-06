f = open("0022_names.txt").read()
names = f.split(",")

names = [name.strip('"') for name in names]
names.sort()

def score(name):
    return sum(ord(c) - ord('A') + 1 for c in name)

total = sum(score(name) * (names.index(name) + 1) for name in names)
print(total)