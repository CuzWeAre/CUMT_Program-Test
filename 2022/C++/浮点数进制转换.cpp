#include<bits/stdc++.h>
using namespace std;
string dtob(double dec,int n)
{
    string bin="0.";
    for(int i=1;i<=n;i++)
    {
        dec*=2;
        int d=int(dec);
        bin+=to_string(d);
        dec-=d;
	}
	return bin;
}
int main()
{
	double decimal_number=0.625;
	string bin=dtob(decimal_number,8);
	cout<<bin;
}

