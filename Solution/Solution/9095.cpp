#include <iostream>
using namespace std;

int DP[100];

int main(){
    int n;
    cin >> n;
    DP[0] = 0;
    DP[1] = 1;
    DP[2] = 2;
    DP[3] = 4;


    for(int i = 4; i<=11; i++){
        DP[i] = DP[i-3] + DP[i-2] + DP[i-1];
    }

    for(int j = 0; j < n; j++){
        int t;
        cin >> t;
        cout << DP[t] << endl;
    }
    return 0;
}