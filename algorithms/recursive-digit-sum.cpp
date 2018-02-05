#include <bits/stdc++.h>

using namespace std;

int digitSum(string n, int k) {
    // Complete this function
    int i;
    k=k%9;
    if(k == 0)
        return 9;
    else
    {
        int sum=0;
        for(i=0;i<n.length();i++)
            sum=(sum+n.at(i)-'0')%9;
        if(((sum%9)*k)%9 == 0)
            return 9;
        else
            return ((sum%9)*k)%9;
     }
}

int main() {
    string n;
    int k;
    cin >> n >> k;
    int result = digitSum(n, k);
    cout << result << endl;
    return 0;
}

