#include<bits/stdc++.h>
using namespace std;
struct stu
{
	string num;
	int grade;
	string name;
}a[100001];
bool cmp(stu a,stu b)
{
	return a.grade<b.grade;
}
int main()
{
	int n,wid[4]={0};
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		cin>>a[i].name>>a[i].num>>a[i].grade;
		wid[1]=max(wid[1],int(a[i].name.size()));
		wid[2]=max(wid[2],int(a[i].num.size()));
	}
	wid[3]=2;
	sort(a+1,a+n+1,cmp);
	for(int i=1;i<=n;i++)
	{
		cout<<setw(wid[1])<<a[i].name<<" ";
		cout<<setw(wid[2])<<a[i].num<<" ";
		cout<<setw(wid[3])<<a[i].grade<<endl;
	}
	return 0;
}
