#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    cin >> n;
    int blanks;
    int hashes;
    for (int i=1;i<=n;i++){
        blanks=n-i;
        hashes=i;
        for(int j=0;j<blanks;j++){
            cout<<" ";
        }
        for(int j=0;j<hashes;j++){
            cout<<"#";
        }
        cout<<endl;
    }
    return 0;
}
