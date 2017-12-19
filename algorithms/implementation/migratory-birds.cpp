#include <bits/stdc++.h>

using namespace std;

int migratoryBirds(int n, vector <int> ar) {
    // Complete this function
    vector <int> res(6,0);
    for(int type:ar) res[type]+=1;
    int max=0;
    int index=0;
    int k=0;
    for(int ans:res){
        if(ans>max){
            max=ans;
            index=k;
        }
        k+=1;
    }
    return index;
}

int main() {
    long int n;
    cin >> n;
    vector<int> ar(n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       cin >> ar[ar_i];
    }
    int result = migratoryBirds(n, ar);
    cout << result << endl;
    return 0;
}
