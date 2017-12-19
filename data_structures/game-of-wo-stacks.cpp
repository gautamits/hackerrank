#include <iostream>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		int n,m,x;
		cin>>n>>m>>x;
		int arr1[n];
		int arr2[m];
		for(int i=0;i<n;i++) cin>>arr1[i];
		for(int i=0;i<m;i++) cin>>arr2[i];
		int i,j,ans,sum=0;
		while(i<n && j<m && sum <= x){
			if(arr1[i] < arr2[j]) {
				ans+=1;
				sum+=arr1[i];
				i+=1;
			}
			else{
				sum+=arr2[j];
				j+=1;
				ans+=1;
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}