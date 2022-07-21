#include<iostream>
#include <string>

using namespace std;

int main() {
    string S;
    cin >> S;
    int start = (int)'a';
    int end = (int)'z';
    for (int i = start; i <= end; i++) {
        int result = S.find((char)i);
        cout << result << " ";
    }
    return 0;
}