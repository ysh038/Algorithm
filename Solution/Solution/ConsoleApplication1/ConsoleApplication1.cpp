/* 10809
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
}*/

/* 1152 */
#include <iostream>
#include <string>

using namespace std;

int main() {
    int result = 0;
    bool word_start = false;
    string S;
    getline(cin, S);
    for (int i = 0; i < S.length(); i++) {
        if (S[i] != ' ' && word_start == false) {
            word_start = true;
        }
        else if (S[i] == ' ' && word_start == true && S[i + 1] != NULL) {
            word_start = false;
            result++;
        }
    }
    bool isBlank = false;
    for (int i = 0; i < S.length(); i++) {
        if (S[i] != ' ')
            isBlank = true;
    }
    if(isBlank){
        result++;
    }
    cout << result;
}