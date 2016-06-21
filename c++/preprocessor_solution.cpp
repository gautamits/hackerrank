#include <climits>
#define INF INT_MAX
#define io(i) cin>>i
#define FUNCTION(f,o) void f(int &a,int &b){a=(a)o(b)?a:b;}
#define toStr(s) #s
#define foreach(a,b) for(int b=0;b<a.size();b++)

#include <iostream>
#include <vector>
using namespace std;
#if !defined toStr || !defined io || !defined FUNCTION || !defined INF
#error Missing preprocessor definitions
#endif

FUNCTION(minimum, <)
FUNCTION(maximum, >)

int main(){
	int n; cin >> n;
	vector<int> v(n);
	foreach(v, i) {
		io(v)[i];
	}
	int mn = INF;
	int mx = -INF;
	foreach(v, i) {
		minimum(mn, v[i]);
		maximum(mx, v[i]);
	}
	int ans = mx - mn;
	cout << toStr(Result =) <<' '<< ans;
	return 0;

}
