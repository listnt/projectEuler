#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool hasValidSplit(const vector<int> &digits, int index, long long currentSum,
                   long long target) {
  // Prune if sum already too large
  if (currentSum > target)
    return false;

  // If all digits are consumed
  if (index == digits.size())
    return currentSum == target;

  long long value = 0;

  for (int i = index; i < digits.size(); i++) {
    value = value * 10 + digits[i];

    if (hasValidSplit(digits, i + 1, currentSum + value, target))
      return true;
  }

  return false;
}

int main() {
  const long long LIMIT = 1000000000000LL;
  long long total = 0;

  long long max_i = static_cast<long long>(sqrt(LIMIT));

  for (long long i = 2; i <= max_i; i++) {
    long long sq = i * i;
    if (sq > LIMIT)
      break;

    // Convert square to digit array
    vector<int> digits;
    long long temp = sq;
    while (temp > 0) {
      digits.push_back(temp % 10);
      temp /= 10;
    }
    reverse(digits.begin(), digits.end());

    if (hasValidSplit(digits, 0, 0, i)) {
      total += sq;
    }
  }

  cout << total << endl;
  return 0;
}
