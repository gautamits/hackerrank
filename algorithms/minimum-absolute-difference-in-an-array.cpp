#include <bits/stdc++.h>

using namespace std;
int diff(int a,int b){
    return abs(a-b);
}
int minimumAbsoluteDifference(int n, vector <int> arr) {
    // Complete this function
    sort(arr.begin(),arr.end());
    int d=arr[1]-arr[0];
    int temp;
    for(int i=0;i<n-1;i++){
        temp=diff(arr[i],arr[i+1]);
        if(d > temp) d=temp;
    }
    return d;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0; arr_i < n; arr_i++){
       cin >> arr[arr_i];
    }
    int result = minimumAbsoluteDifference(n, arr);
    cout << result << endl;
    return 0;
}

