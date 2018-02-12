#include <iostream>
#include <cstring>
using namespace std;
int main(){
    int arr[26];
    for(int i=0;i<26;i++){
        cin>>arr[i];
    }
    char word[11];
    cin>>word;
    int max=0;
    for(int i=0;i<strlen(word);i++){
        if(arr[word[i]-97] > max){
            max=arr[word[i]-97];
        }
    }
    cout<<(max*strlen(word))<<endl;

}