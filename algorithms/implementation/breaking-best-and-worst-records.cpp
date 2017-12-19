#include <bits/stdc++.h>

using namespace std;

vector < int > getRecord(vector < int > s){
    // Complete this function
    int mi=s[0];
    int ma=s[0];
    int count_min=0;
    int count_max=0;
    for(int i=1;i<s.size();i++){
        if(s[i]<mi){
            mi=s[i];
            count_min++;
        }
        else if(s[i]>ma){
            ma=s[i];
            count_max++;
        }
    }
    vector <int> answer(2);
    answer[0]=count_max;
    answer[1]=count_min;
    return answer;
}

int main() {
    int n;
    cin >> n;
    vector<int> s(n);
    for(int s_i = 0; s_i < n; s_i++){
       cin >> s[s_i];
    }
    vector < int > result = getRecord(s);
    string separator = "", delimiter = " ";
    for(auto val: result) {
        cout<<separator<<val;
        separator = delimiter;
    }
    cout<<endl;
    return 0;
}
