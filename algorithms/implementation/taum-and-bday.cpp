#include <bits/stdc++.h>

using namespace std;

long int taumBday(long int b, long int w, long int x, long int y, long int z) {
    // Complete this function
    if(x > y+z) return b*(y+z)+w*y;
    if(y > x+z) return b*x+w*(x+z);
    return b*x+w*y;
}

int main() {
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        long int b;
        long int w;
        cin >> b >> w;
        long int x;
        long int y;
        long int z;
        cin >> x >> y >> z;
        long int result = taumBday(b, w, x, y, z);
        cout << result << endl;
    }
    return 0;
}
