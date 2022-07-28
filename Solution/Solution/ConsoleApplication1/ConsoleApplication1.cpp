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

/* 1152
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
} */
 /*1712
#include<iostream>

using namespace std;

int main() {
    int fixed_cost = 0;
    int variable_cost = 0;
    int price = 0;
    int result;
    scanf("%d %d %d", &fixed_cost, &variable_cost, &price);
    if (variable_cost >= price) {
        printf("-1");
        return 0;
    }
    else {
        result = fixed_cost / (price - variable_cost);
    }
    printf("%d", ++result);
    return 0;
}*/
/*2869
#include <iostream>
using namespace std;

int main() {
    int speed = 0, slip = 0, distance = 0, result = 0;
    scanf("%d %d %d", &speed, &slip, &distance);
    distance = distance - speed;
    result = (distance / (speed - slip)) + 1;
    if (distance % (speed - slip) == 0) {
        
    }
    else {
        result++;
    }
    printf("%d", result);
    return 0;
}
*/
/*10250
#include<iostream>
using namespace std;

int main() {
    int height = 0, width = 0, num = 0,test_num = 0;
    int result = 0;
    scanf("%d", &test_num);

    for (int test_count = 0; test_count < test_num; test_count++) {
        scanf("%d %d %d", &height, &width, &num);
        if (num % height != 0) {
            result = (num % height)*100 + (num / height + 1);
        }
        else {
            result = height*100 + (num / height);
        }

        cout << result << endl;
    }
}*/