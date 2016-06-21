
#include<iostream>
#include<stack>
using namespace std;
int getMaxArea(int hist[], int n)
{
   
    stack<int> s;
 
    int max_area = 0; // Initalize max area
    int tp;  // To store top of stack
    int area_with_top; // To store area with top bar as the smallest bar
 
    
    int i = 0;
    while (i < n)
    {
 
        if (s.empty() || hist[s.top()] <= hist[i])
            s.push(i++);
 
        
        else
        {
            tp = s.top(); 
            s.pop(); 
 
     
            area_with_top = hist[tp] * (s.empty() ? i : i - s.top() - 1);
 
           
            if (max_area < area_with_top)
                max_area = area_with_top;
        }
    }
 
   
    while (s.empty() == false)
    {
        tp = s.top();
        s.pop();
        area_with_top = hist[tp] * (s.empty() ? i : i - s.top() - 1);
 
        if (max_area < area_with_top)
            max_area = area_with_top;
    }
 
    return max_area;
}
 
// Driver program to test above function
int main()
{
    int n;
    cin>>n;
    int m=n;
    int arr[n];
    int i=0;
    while (n >0){
    	cin>>arr[i];
    	i+=1;
    	n-=1;
    	}
    cout << getMaxArea(arr, m)<<endl;
    return 0;
}
