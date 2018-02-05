#include <bits/stdc++.h>
using namespace std;

int powerSum(int X, int P, int N=1) {
    int i_pow = pow(N,P);
    if (i_pow > X)
        return 0;
    else if (i_pow == X)
        return 1;
      // subproblem
    return powerSum(X,P,N+1) + powerSum(X-i_pow,P,N+1);
}

int main() {
    int X;
    cin >> X;
    int N;
    cin >> N;
    int result = powerSum(X, N);
    cout << result << endl;
    return 0;
}

