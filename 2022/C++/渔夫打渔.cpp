#include<bits/stdc++.h>
using namespace std;
struct date
{
	int yy;
	int mm;
	int dd;
};
int mon[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
int is_le(int a)
{
	if((a%4==0&&a%100!=0)||(a%400==0))
		return 1;
	return 0;
}
int interval(date a,date b)
{
	int s=0,e=0,d=0;
	for(int i=a.yy+1;i<b.yy;i++)
	{
		if(is_le(i))
			d+=366;
		else
			d+=365;
	}
	int flag1=is_le(a.yy),flag2=is_le(b.yy);
	for(int i=a.mm+1;i<=12;i++)
	{
		if(flag1==1&&i==2)
			s+=29;
		else
			s+=mon[i];
	}
	s+=mon[a.mm]-a.dd+1;
	if(a.mm==2&&flag1==1)
		s+=1;
	for(int i=1;i<=b.mm-1;i++)
	{
		if(flag2==1&&i==2)
			e+=29;
		else
			e+=mon[i];
	}
	e+=b.dd;
	if(a.yy!=b.yy)
		return e+s+d;
	else
		return e+s-365;
}
//这题C++真的是被python按在地上踩 
int main()
{
	date st,ed;
	cin>>st.yy>>st.mm>>st.dd;
	cin>>ed.yy>>ed.mm>>ed.dd;
	int intv=interval(st,ed);
	printf("经过%d天",intv);
	int wd=(intv/5)*3;
	wd+=intv%5<3?intv%5:3;
	printf("打渔%d天，摸鱼%d天",wd,intv-wd);	
	return 0;
}
