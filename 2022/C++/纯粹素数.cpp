#include<bits/stdc++.h>
using namespace std;
bool is_prime(int n)
{
	if(n==2||n==3)
		return 1;
	for(int i=2;i*i<=n;i++)
	{
		if(n%i==0)
			return 0;
	}
	return 1;
}
int toi(string s,int a)
{
	int n=0;
	for(int i=a;i<s.size();i++)
	{
		n*=10;
		n+=int(s[i]-'0');
	}
	return n;
}
int main()
{
	string n;
	int flag=1;
	cin>>n;
	for(int i=0;i<n.size();i++)
	{
		if(is_prime(toi(n,i))==0)
		{
			flag=0;
			break;
		}
	}
	if(flag==1)
		cout<<n<<"是纯粹素数"; 
	else
		cout<<n<<"不是纯粹素数"; 
	return 0;
}
