#include <bits/stdc++.h>

using namespace std;

int sockMerchant(int n, vector <int> ar) {
    // Complete this function
    int sum=0;
    int arr[101];
    for(int i=0;i<=100;i++) arr[i]=0;
    for(int i=0;i<ar.size();i++){
        if(arr[ar[i]]==0) arr[ar[i]]=1;
        else{
            arr[ar[i]]=0;
            sum++;
        }
    }
    return sum;
}

int main() {
    int n;
    cin >> n;
    vector<int> ar(n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       cin >> ar[ar_i];
    }
    int result = sockMerchant(n, ar);
    cout << result << endl;
    return 0;
}