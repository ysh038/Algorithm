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
/*2839
#include <iostream>
using namespace std;

int main() {
    int N = 0 , result = 0;
    cin >> N;

    while (N > 0) {
        if (N % 5 == 0) {
            result += N / 5;
            cout << result << endl;
            return 0;
        }
        N -= 3;
        result++;

        if (N < 0) {
            cout << -1 << endl;
            return 0;
        }
    }
    cout << result << endl;
    return 0;
}*/
/*1978*/
/*#include <iostream>
using namespace std;

int findNum(int num) {
    if (num < 2)
        return 0;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0)
            return 0;
    }
    return 1;
}

int main() {
    int number = 0, result = 0;
    cin >> number;
    int* num_arr = new int[number];
    for (int i = 0; i < number; i++) {
        cin >> num_arr[i];
        result += findNum(num_arr[i]);
    }
    cout << result;
}*/
/*2581
#include <iostream>
using namespace std;

int Function(int num) {
    if (num < 2) {
        return 0;
    }
    for (int j = 2; j * j <= num; j++) {
        if (num % j == 0) {
            return 0;
        }
    }
    return num;
}

int main() {
    int m = 0, n = 0;
    bool isFirst = true;
    int result = 0, min = -1;

    cin >> m >> n;

    for (int i = m; i <= n; i++) {
        result+=Function(i);
        if (isFirst && Function(i) != 0) {
            min = Function(i);
            isFirst = false;
        }
    }
    if (min == -1) {
        cout << -1 << endl;
    }
    else {
        cout << result << endl;
        cout << min << endl;
    }
    return 0;
}*/
/*1929
#include <iostream>
using namespace std;

int number = 1000000;
int a[1000001];

void Find() {
    for (int i = 2; i <= number; i++) {
        a[i] = i;
    }
    for (int i = 2; i <= number; i++) {
        if (a[i] == 0) continue;
        for (int j = i + i; j <= number; j += i) {
            a[j] = 0;
        }
    }
}

int main() {
    int start = 0, end = 0;
    cin >> start >> end;
    Find();
    for (int i = start; i <= end; i++) {
        if (a[i] != 0)
            cout << a[i] << '\n';
    }
    return 0;
}*/

/*10872
#include <iostream>
using namespace std;

void Factorial(int n,int result) {
    if (n == 0) {
        cout << result << endl;
    }
    else {
        result *= n;
        Factorial(--n, result);
    }
}

int main() {
    int n = 0;
    cin >> n;
    int result = 1;

    Factorial(n,result);
    return 0;
}*/
/*17478
#include<iostream>
using namespace std;

void PrintUnderBar(int repeat) {
        for (int i = repeat; i > 0; i--) {
            printf("____");
        }
}
void ChatBot(int n,int repeat) {
    if (n > 1) {
        PrintUnderBar(repeat);
        printf("\"재귀함수가 뭔가요?\"\n");
        PrintUnderBar(repeat);
        printf("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n");
        PrintUnderBar(repeat);
        printf("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n");
        PrintUnderBar(repeat);
        printf("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n");
        ChatBot(n-1, repeat+1);
    }
    else {
        PrintUnderBar(repeat);
        printf("\"재귀함수가 뭔가요?\"\n");
        PrintUnderBar(repeat);
        printf("\"재귀함수는 자기 자신을 호출하는 함수라네\"\n");
    }                      

    PrintUnderBar(repeat);
    printf("라고 답변하였지.\n");
}

int main() {
    int n = 0, repeat = 1;
    cin >> n;

    printf("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n");
    printf("\"재귀함수가 뭔가요?\"\n");
    printf("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n");
    printf("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n");
    printf("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n");

    ChatBot(n,repeat);
    printf("라고 답변하였지.");
    return 0;
}*/
/*2798
#include <iostream>
using namespace std;

int main() {
    int N = 0, M = 0;
    cin >> N >> M;
    int* card = new int[N];
    int result = 0;
    for (int i = 0; i < N; i++) {
        cin >> card[i];
    }
    for (int i = 0; i < N - 2; i++) {
        for (int j = i + 1; j < N - 1; j++) {
            for (int k = j + 1; k < N; k++) {
                if (card[i] + card[j] + card[k] <= M && M - (card[i] + card[j] + card[k]) < M - result) {
                    result = card[i] + card[j] + card[k];
                }
            }
        }
    }
    cout << result;
}*/