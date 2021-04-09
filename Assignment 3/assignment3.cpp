/*          ASSIGNMENT - 3 | Zelthy - Hemant kumar Lader(hemantlader@gmail.com)
*
*   Input format:
*       first line is an integer denoting no. of elements in array1 (n)
*       second line contains n space separated integers denoting elements of A
*       third line is an integer denoting no. of elements in array2 (m)
*       fourth line contains 'm' space separated integers denoting elements of B
*      Ex. 
            INPUT:
*               12
*               3 6 7 4 2 7 9 1 0 3 5 6
*               12
*               1 5 6 9 7 4 2 7 9 9 2 1
*           OUTPUT:
*               7 4 2 7 9
*
*/

#include <bits/stdc++.h>
using namespace std;

void SimElement(vector<int> &A, vector<int> &B )
{
    int maxm = INT_MIN;
    int m = A.size(), n = B.size();
    bool found = false;
    int maxi=0, maxj =0;
    
    vector<vector<int>>  dp(m+1,vector<int>(n+1, 0));
    for(int i = 1; i <= m; ++i) {
        for(int j = 1;j <= n; ++j) {
            if(B[i-1] == A[j-1]){
                dp[i][j] = dp[i-1][j-1] + 1;
                if(maxm < dp[i][j]) {
                    maxm = dp[i][j];
                    maxi = i;
                    maxj = j;
                    found = true;
                }
            }
        }
    }
    if(found) {
        stack<int> ans;
        int i = maxi, j = maxj;
        while(i-1 >=0 && j-1 >=0 && dp[i][j] != 0) {
            ans.push(A[j-1]);
            i--; j--;
        }
        while(!ans.empty()){
            cout<<ans.top()<<" ";
            ans.pop();
        }
    }
}
int main()
{
    int n, m, t;
    vector<int> A, B;
    cin>>n;
    while(n--){
        cin>>t;
        A.push_back(t);
    }
    cin>>m;
    while(m--){
        cin>>t;
        B.push_back(t);
    }
    SimElement(A, B);
}