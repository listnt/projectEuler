package main

import (
	"fmt"
	"math"
)

func divisors(n int64) int64 {
	var count int64 = 0
	root := int64(math.Sqrt(float64(n)))
	for i := int64(1); i <= root; i++ {
		if n%i == 0 {
			count += 2
		}
	}
	if root*root == n {
		count-- // perfect square fix
	}
	return count
}

func main() {
	t := int64(28)
	for i := int64(8); i < 1000000; i++ {
		t += i
		if i < 5000 {
			continue
		}

		divs := divisors(t)
		fmt.Println(i, t, divs)

		if divs > 500 {
			fmt.Println("Answer:", t)
			break
		}
	}
}
