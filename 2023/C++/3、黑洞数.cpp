#include<bits/stdc++.h>
using namespace std;
int a[5];
bool cmp(int x,int y)
{
	return x>y;
}
int main()
{
	int n;
	cin>>n;
	for(int i=1;i<=4;i++)
	{
		a[i]=n%10;
		n/=10;
	}
	int ans=0,cnt=0;
	while(ans!=6174)
	{
		cnt++;
		int minn=0,maxn=0;
		sort(a+1,a+5);
		for(int i=1;i<=4;i++)
		{
			minn*=10;
			minn+=a[i];
		}
		sort(a+1,a+5,cmp);
		for(int i=1;i<=4;i++)
		{
			maxn*=10;
			maxn+=a[i];
		}
		ans=maxn-minn;
		cout<<ans<<endl;
		int tmp=ans;
		for(int i=1;i<=4;i++)
		{
			a[i]=tmp%10;
			tmp/=10;
		}
	}
	cout<<cnt;
	return 0;
}
