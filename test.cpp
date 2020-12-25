#include<bits/stdc++.h>
#define int long long
#define X first
#define Y second
#define lson (root<<1)
#define rson (root<<1|1)
#define ALL(x) x.begin(),x.end()
#define CLR(x,y) memset(x,y,sizeof(x))
//#define endl '\n'
using namespace std;
typedef pair<int,int> pii;
int a[3][3]
{
	{1,1,1},
	{1,0,1},
	{1,1,1}
};
signed main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n=3,m=3;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			printf("let tmparr=img[%lld];let tmparr[%lld]=%lld;\n",i,j,a[i][j]);
		}
	}
	return 0;
}
