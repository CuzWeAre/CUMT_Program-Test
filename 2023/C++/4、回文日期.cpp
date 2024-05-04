#include<bits/stdc++.h>
using namespace std;
bool is_valid(int yyyy,int mm,int dd)
{
	if(1000<yyyy<=9999&&1<=mm<=12)
	{
		if((mm==1||mm==3||mm==5||mm==7||mm==8||mm==10||mm==12)&&1<=dd<=31)
			return 1;
		else if((mm==4||mm==6||mm==9||mm==11)&&1<=dd<=30)
			return 1;
		else if(mm==2&&1<=dd<=29)
			return 1;
		else return 0;
	}
	return 0;
}
int main()
{
	int daytime,year,month,day;
	cin>>daytime;
	year=daytime/10000;
	month=(daytime-year*10000)/100;
	day=daytime%100;
	while(year<=9999)
	{
		year+=1;
		month=year%10*10+year/10%10;
		day=year/100%10*10+year/1000;
		daytime=year*10000+year%10*1000+year/10%10*100+year/100%10*10+year/1000; 
		if(is_valid(year,month,day))
		{	
			printf("%d",daytime);
			break;
		}
	}
	return 0;
}
