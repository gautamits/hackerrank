#include <iostream>
using namespace std;
int main(){
	int n1,n2,n3;
	cin>>n1>>n2>>n3;
	int arr1[n1];
	int arr2[n2];
	int arr3[n3];
	for(int i=n1-1;i>=0;i--) cin>>arr1[i];
	for(int i=n2-1;i>=0;i--) cin>>arr2[i];
	for(int i=n3-1;i>=0;i--) cin>>arr3[i];
	//cout<<"solving\n";
	int sum=0;
	for(int i=0;i<n1;i++) arr1[i]=sum+=arr1[i];
	sum=0;
	for(int i=0;i<n2;i++) arr2[i]=sum+=arr2[i];
	sum=0;
	for(int i=0;i<n3;i++) arr3[i]=sum+=arr3[i];
	int i,j,k;
	i=n1-1;
	j=n2-1;
	k=n3-1;
	while(1){
		if(arr1[i]==arr2[j] && arr2[j]==arr3[k] || i==0 || j==0 || k==0) break;
		else if(arr1[i] > arr2[j] || arr1[i] > arr3[k]) i-=1;
		else if(arr2[j] > arr1[i] || arr2[j] > arr3[k]) j-=1;
		else k-=1;
	}
	if(i<0 || j<0 || k<0) cout<<"0\n";
	else if(arr1[i]==arr2[j] && arr2[j]|| arr3[k]) cout<<arr1[i]<<endl;
	else cout<<<<endl;

}