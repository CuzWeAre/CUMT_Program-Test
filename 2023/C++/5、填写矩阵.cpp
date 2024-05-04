#include<bits/stdc++.h>
using namespace std;
int a[1001][1001];
int vis[1001][1001];
int main()
{
	int n,x=1,y=1,pos1=0,pos2=1,cnt;
	cin>>n;
	n-=1;
	cnt=1;
	for(int i=1;i<=n*n;i++)
	{
		a[x][y]=cnt;
		vis[x][y]=1;
		if(pos2==1&&(y==n||vis[x+pos1][y+pos2]))
		{
			pos2=0;
			pos1=1;
		}
		else if(pos1==1&&(x==n||vis[x+pos1][y+pos2]))
		{
			pos2=-1;
			pos1=0;
		}
		else if(pos2==-1&&(y==1||vis[x+pos1][y+pos2]))
		{
			pos2=0;
			pos1=-1;
		}
		else if(pos1==-1&&(x==2||vis[x+pos1][y+pos2]))
		{
			pos1=0;
			pos2=1;
			cnt+=1;
		}
		x+=pos1;
		y+=pos2;
	}
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=n;j++)
		{
			printf("%d ",a[i][j]);
		}
		printf("\n");
	}
	return 0;
}
