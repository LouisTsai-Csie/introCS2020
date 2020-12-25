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
string a[15]
{
	"111111111111111",
	"111111111111111",
	"111000000000011",
	"111000000000011",
	"111000000000011",
	"111000000000011",
	"111000000000011",
	"111000000000011",
	"111000000000011",
	"111000000000011",
	"111000000000011",
	"111000000000011",
	"111000000000011",
	"111000000000011",
	"111111111111111"
};
signed main()
{
	int n=15,m=15;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			printf("let tmpArray=img[%lld];let tmpArray[%lld]=%lld;",i,j,(int)(a[i][j]-'0'));
		}
		printf("\n");
	}
	return 0;
}
