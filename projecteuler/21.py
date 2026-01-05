# func divisors(n int64) []int64 {
# 	divs := []int64{}
# 	root := int64(math.Sqrt(float64(n)))
# 	for i := int64(1); i <= root; i++ {
# 		if n%i == 0 {
# 			divs = append(divs, i)
# 			divs = append(divs, n/i)
# 		}
# 	}
# 	if root*root == n {
# 		divs = divs[:len(divs)-1] // perfect square fix
# 	}

# 	return divs
# }

def divisors(n):
    divs = [1]
    root = int(n**0.5)
    for i in range(2, root + 1):
        if n % i == 0:
            divs.append(i)
            divs.append(n // i)
    if root * root == n:
        divs = divs[:-1]  # perfect square fix
    return divs

sums=0

for i in range(5,10000):
    divs = divisors(i)
    ammicable = sum(divs)
    if i==220:
        print(i,divisors(i),ammicable,divisors(ammicable))
    if sum(divisors(ammicable))==i and ammicable != i:
        print(i, ammicable)
        sums+=i
print(sums)