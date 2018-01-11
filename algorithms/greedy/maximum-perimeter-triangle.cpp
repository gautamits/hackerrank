#include <bits/stdc++.h>

using namespace std;

int maximumPerimeterTriangle(vector <int> l) {
    // Complete this function
    sort(l.begin(),l.end());
    int i;
    bool ans=1;
    for(i=l.size()-3;i>=0;i--){
        if(l[i]+l[i+1]>l[i+2]){
            break;
        }
    }
    if(i>=0) cout<<l[i]<<" "<<l[i+1]<<" "<<l[i+2]<<endl;
    else cout<<"-1\n";
    return 0;
}

int main() {
    int n;
    cin >> n;
    vector<int> l(n);
    for(int l_i = 0; l_i < n; l_i++){
       cin >> l[l_i];
    }
    int result = maximumPerimeterTriangle(l);
    


    return 0;
}