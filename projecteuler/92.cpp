// g++ 92.cpp -o .exe
// ./.exe

#include <iostream>
using namespace std;

int nextNumber(int x) {
  int sum = 0;
  while (x > 0) {
    int digit = x % 10;
    sum += digit * digit;
    x /= 10;
  }
  return sum;
}

int main() {
  int count = 0;

  for (int i = 2; i <= 10000000; i++) {
    int x = i;

    while (x != 1 && x != 89) {
      x = nextNumber(x);
    }

    if (x == 89) {
      count++;
    }
  }

  cout << count << endl;
  return 0;
}
