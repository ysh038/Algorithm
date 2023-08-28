#include <iostream>
using namespace std;

int DP[41] = {0,1,1};

int main(){
    int n,t;
    cin >> n;
    for(int i = 3; i < 41; i++){
        DP[i] = DP[i-1] + DP[i-2];
    }

    for(int i=0; i<n; i++){
        cin>>t;
        if(t == 0)
            cout << 1 << ' ' << 0 << '\n';
        else if(t == 1)
            cout << 0 << ' ' << 1 << '\n';
        else
            cout << DP[t-1] << ' ' << DP[t] << '\n';
    }
}