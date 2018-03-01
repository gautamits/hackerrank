#include <bits/stdc++.h>

using namespace std;

int theLoveLetterMystery(string s){
    // Complete this function
	int n=s.length();
	int m=n/2;
	int sum=0;
	int i=0;
	n-=1;
	while(i<=m && n >= m){
		sum+=abs(s[i]-s[n]);
		i+=1;
		n-=1;
	}
	return sum;
}

int main() {
    int q;
    cin >> q;
    for(int a0 = 0; a0 < q; a0++){
        string s;
        cin >> s;
        int result = theLoveLetterMystery(s);
        cout << result << endl;
    }
    return 0;
}
