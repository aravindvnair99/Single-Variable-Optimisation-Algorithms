//Bounding Phase Method
#include<bits/stdc++.h>
#include <cmath>
using namespace std;
float f(float x)
{
    //y=x^2 +54/x;
    return x*x + 54/x;
}
int main()
{
    int i=0;
    float x[20]={0},d;
    cout<<"Input initial point and delta ";
    cin>>x[0]>>d;
    cout<<"power "<<pow(2,3);
    if((f(x[0]-d)>f(x[0])) && (f(x[0]+d)>f(x[0])))
    {
        cout<<"Minimum lies between "<<x[0]-d<<" and "<<x[0]+d;
        exit(1);
    }
    else if(f(x[0]-d)<f(x[0]+d))
    {   
        d=d*(-1);
    }
    do
    {
        i++;
        x[i]=x[i-1] + pow(2,i-1)*d;
    }while(f(x[i])<f(x[i-1]));
    if(d<0) cout<<"Minimum lies between "<<x[i]<<" and "<<x[i-2];
    else cout<<"Minimum lies between "<<x[i-2]<<" and "<<x[i];
}
