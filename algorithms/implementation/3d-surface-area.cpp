#include <bits/stdc++.h>
#include <vector>
using namespace std;
int main(){
	int m,n;
	cin>>m>>n;
	vector <vector<int>> board;
	for(int i=0;i<m;i++){
		board.push_back(vector <int>());
		for(int j=0;j<n;j++){
			int temp;
			cin>>temp;
			board[i].push_back(temp);
		}
	}
	
	int sum=0;
	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++){
			if(board[i][j] > 0){
				//count upper and lower surface
				sum+=2;
			}
			if(i==0){
				//side most
				sum += board[i][j];
			}
			if(j==0){
				//top-bottom most
				sum+= board[i][j];
			}
			if(i==m-1) sum+=board[i][j];
			if(j==n-1) sum+=board[i][j];
			if(i>=0 && i < m-1){
				//middle, count right and bottom
				sum+=abs(board[i][j]-board[i+1][j]);
			}
			if(j >=0 && j < n-1){
				sum+=abs(board[i][j]-board[i][j+1]);	
			}
		}
	}
	cout<<sum<<endl;
}
