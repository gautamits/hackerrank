//https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
#include <bits/stdc++.h>

using namespace std;

string catAndMouse(int x, int y, int z) {
    // Complete this function
    if(abs(x-z) < abs(y-z)) return "Cat A";
    else if(abs(y-z) < abs(x-z) ) return "Cat B";
    else return "Mouse C";
}

int main() {
    int q;
    cin >> q;
    for(int a0 = 0; a0 < q; a0++){
        int x;
        int y;
        int z;
        cin >> x >> y >> z;
        //vector <string> result = catAndMouse(x, y, z);
        //for (ssize_t i = 0; i < result.size(); i++) {
        //    cout << result[i] << (i != result.size() - 1 ? " " : "");
        //}
        cout<<catAndMouse(x,y,z);
        cout << endl;


    }
    return 0;
}
