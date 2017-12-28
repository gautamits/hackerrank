#include <bits/stdc++.h>

using namespace std;

long solve(long n) {
    // Complete this function
    long t=0;
    while(n>0){
        t=t+!(n&1);
        n=n>>1;
        
    }
    return pow(2,t);
}

int main() {
    long n;
    cin >> n;
    long result = solve(n);
    cout << result << endl;
    return 0;
}
