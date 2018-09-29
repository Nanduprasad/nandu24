#include <stdio.h>
int main()
{
	int n,i,x=1,pow=2;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
	    x=x*pow;
	    if(x==n)
	    {
	        printf("yes");
	        break;
	    }
	}
        if(x!=n)
	    {
	        printf("no");
	    }
	return 0;
}
