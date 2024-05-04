#include<bits/stdc++.h>
using namespace std;
vector<int>a,ans;
bool is_Hprime(int n)
{
	for(int i=0;i<a.size();i++)
		if(n%a[i]==0)
			return 0;
	return 1;
}
int main()
{
	a.push_back(5);
	for(int i=9;i<=40;i+=4)
		if(is_Hprime(i))
			a.push_back(i);
	for(int i=0;i<a.size();i++)
		for(int j=i;j<a.size();j++)
		{
			if(a[i]*a[j]<150)
				ans.push_back(a[i]*a[j]);
		}
	sort(ans.begin(),ans.end());
	for(int i=0;i<ans.size();i++)
		cout<<ans[i]<<endl;
	return 0;
}
