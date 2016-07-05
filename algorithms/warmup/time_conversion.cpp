#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int h;
    int minutes;
    int seconds;
    char mode[2];
    char sep;
    scanf("%d%c%d%c%d%s",&h,&sep,&minutes,&sep,&seconds,mode);
    if(!strcmp(mode,"PM") && h != 12)h+=12;
    if(!strcmp(mode,"AM") && h == 12)h = 0;
    printf("%02d:%02d:%02d\n",h,m,s);
}
