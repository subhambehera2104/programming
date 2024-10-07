#include<stdio.h>
void frequencyNum(int num[], int n, int frequency[])
{
   
    for(int i=0; i<n; i++)
    {
        frequency[i]=1;
    }
    for(int i =0; i<n; i++)
    {
        if(frequency[i]==-1)
        {
            continue;
        }
        for(int j = i+1; j<n; j++)
        {
            if(num[i]==num[j])
            {
                frequency[i]++;
                frequency[j]=-1;
            }
        }
    }
}
int main()
{
    int num[] = {1, 4, 2, 0, 1, 4};
    int n = sizeof(num)/sizeof(num[0]);
    int res[n];
    
    frequencyNum(num, n, res);
    for(int i = 0; i<n; i++)
    {
        if(res[i]!=-1)
        {
            printf("key %d value %d\n",num[i],res[i]);
        }
    }
   
    return 0;
}