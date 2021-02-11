//Exhaustive Search Algorithm
#include<bits/stdc++.h> 
using namespace std;
float f(float x)
{
    //y=x^2 +54/x;
    return x*x + 54/x;
}
int main()
{
    float a,b,n,x1,x2,x3,d;
    cout<<"Input lower limit and upper limit to find minimum in the interval (a,b) ";
    cin>>a>>b;
    cout<<"Input number of intervals ";
    cin>>n;
    d=(b-a)*1.0/n;
    x1=a;
    x2=x1+d;
    x3=x2+d;
    while(!((f(x1)>=f(x2))&&(f(x2)<f(x3))))
    {
        x1=x2;
        x2=x3;
        x3=x2+d;
    }
    if(x3<=b)cout<<"Minimum lies in the interval "<<x1<<" and "<<x3<<endl;
    else cout<<"No minimum exists in the given interval or the boundary point is the minimum point."<<endl;
}
