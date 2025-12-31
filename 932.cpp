// g++ -O3 -fopenmp 932.cpp -o .exe

#include <bits/stdc++.h>
#include <omp.h>

using namespace std;

int main() {
  const long long R = 10000000000000000LL; // 1e16
  long long n = 0;

  long long max_i = sqrt((long double)R);

#pragma omp parallel
  {
    long long local_sum = 0;

#pragma omp for schedule(dynamic)
    for (long long i = 0; i <= max_i; ++i) {
      long long sq = i * i;
      if (sq > R)
        continue;

      string s = to_string(sq);
      int len = s.size();

      for (int k = 1; k < len; ++k) {
        if (s[k] == '0')
          continue;

        long long l = stoll(s.substr(0, k));
        long long r = stoll(s.substr(k));

        long long sum = l + r;
        if (sum * sum == sq) {
          local_sum += sq;
        }
      }
    }

#pragma omp atomic
    n += local_sum;
  }

  cout << n << endl;
  return 0;
}
