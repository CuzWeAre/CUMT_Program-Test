#include<bits/stdc++.h>
using namespace std;
int a[101][101];
int vis[101][101];
int n;
int main()
{
	scanf("%d",&n);
	int x=1,y=1,pos1=0,pos2=1;
	memset(a,0,sizeof(a));
	for(int i=1;i<=n*n;i++)
	{
		if(vis[x][y]==0)
		{
			a[x][y]=i;
			vis[x][y]=1;
		}
		if(pos2==1&&(y+pos2>n||vis[x+pos1][y+pos2]!=0))
		{
			pos1=1;
			pos2=0;
		}
		if(pos1==1&&(x+pos1>n||vis[x+pos1][y+pos2]!=0))
		{
			pos1=0;
			pos2=-1;
		}
		if(pos1==-1&&(x+pos1<=0||vis[x+pos1][y+pos2]!=0))
		{
			pos1=0;
			pos2=1;
		}		
		if(pos2==-1&&(y+pos2<=0||vis[x+pos1][y+pos2]!=0))
		{
			pos1=-1;
			pos2=0;
		}
		x+=pos1;
		y+=pos2;
	}
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=n;j++)
		{
			printf("%02d ",a[i][j]);
		}
		printf("\n");
	}
}
