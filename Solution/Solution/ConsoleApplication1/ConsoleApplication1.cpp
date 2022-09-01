/* 10809 알파벳찾기
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

/* 1152 단어의 개수
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
 /*1712 손익분기점
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
/*2869 달팽이는 올라가고싶다
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
/*10250 ACM호텔
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
/*2839 설탕 배달
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
/* 1978 소수찾기 */
/*
#include <iostream>
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
}
*/
/* 2581 소수
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
/*1929 소수 구하기
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

/*10872 팩토리얼
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
/*17478 재귀함수가 뭔가요?
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
/*2798 블랙잭
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
/*2750 수 정렬하기 Bubble Sort
#include <iostream>
using namespace std;

void swap(int* first, int* second) {
    int temp = *second;
    *second = *first;
    *first = temp;
}

int main() {
    int N;
    cin >> N;
    int* arr = new int[N];

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < N; i++) {
        for (int j = 1; j < N - i; j++) {
            if (arr[j - 1] > arr[j]) {
                swap(&arr[j - 1], &arr[j]);
            }
        }
    }
    
    for (int i = 0; i < N; i++) {
        cout << arr[i] << "\n";
    }
    return 0;
}*/
/*2750 수 정렬하기 Insertion Sort
#include <iostream>
using namespace std;

void swap(int* first, int* second) {
    int temp = *second;
    *second = *first;
    *first = temp;
}

int main() {
    int N;
    cin >> N;
    int* arr = new int[N];

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    for (int i = 1; i < N; i++) {
        for (int j = i-1; j >= 0; j--) {
            if (arr[j+1] < arr[j]) {
                swap(&arr[j + 1], &arr[j]);
            }
        }
    }

    for (int i = 0; i < N; i++) {
        cout << arr[i] << "\n";
    }
    return 0;
}*/
/*2751 수 정렬하기2 분할정복 Merge Sort
#include <iostream>
using namespace std;

//int temp[1000000];

void merge(int* arr, int* temp, int left, int right) {
    int n = right - left + 1;
    int mid = (left + right) / 2;
    int i = left;
    int k = left;
    int j = mid + 1;

    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp[k] = arr[i];
            k++;
            i++;
        }
        else if (arr[i] > arr[j]) {
            temp[k] = arr[j];
            k++;
            j++;
        }
    }

    while (i <= mid) {
        temp[k] = arr[i];
        k += 1;
        i += 1;
    }

    while (j <= right) {
        temp[k] = arr[j];
        j += 1;
        k += 1;
    }

    for (int index = left; index <= right; index++) {
        arr[index] = temp[index];
    }
}

void mergeSort(int* array, int *temp, int left, int right) {
    if (left != right) {
        mergeSort(array, temp, left, (left + right) / 2);
        mergeSort(array, temp, (left + right) / 2 + 1, right);
        merge(array, temp, left, right);
    }
}


int main() {
    int n = 0;
    cin >> n;
    int* arr = new int[n];
    int* temp = new int[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    mergeSort(arr,temp, 0, n - 1);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << "\n";
    }
    return 0;
}*/
/*10809 수 정렬하기3 카운팅 정렬
#include <iostream>
using namespace std;

int main() {
    int temp[10001] = {0,};
    int N = 0;    
    int a = 0;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d", &a);
        temp[a - 1] += 1;
    }

    for (int i = 0; i < 10000; i++) {
        while (temp[i] > 0) {
            printf("%d\n", i + 1);
            temp[i]--;
        }
    }
    return 0;
}*/
/*2108 통계학  정렬
#include <iostream>
using namespace std;

void merge(int* array, int* temp, int left, int right) {
    int n = right - left + 1;
    int middle = (right + left) / 2;
    int i = left;
    int k = left;
    int j = middle + 1;
    while (i <= middle && j <= right) {
        if (array[i] > array[j]) {
            temp[k] = array[j];
            k++;
            j++;
        }
        else {
            temp[k] = array[i];
            k++;
            i++;
        }
    }
    while (i <= middle) {
        temp[k] = array[i];
        k++;
        i++;
    }
    while (j <= right) {
        temp[k] = array[j];
        j++;
        k++;
    }
    for (int a = left; a <= right; a++) {
        array[a] = temp[a];
    }
}

void mergeSort(int *array,int *temp, int left, int right) {
    if (left != right) {
        mergeSort(array, temp, left, (left + right) / 2);
        mergeSort(array, temp, (left + right) / 2 + 1, right);
        merge(array, temp, left, right);
    }
}

int findMostUsed(int* array, int N) {
    if (N == 1) {
        return array[0];
    }
    else if (N == 2) {
        return array[1];
    }
    int* most = new int[N];
    most = { 0, };
    int most_count = 0;
    int count = 0;
    int i = 0;
    int k = 0;
    while (i < N) {
        if (array[i] == array[i + 1]) {
            count++;
        }
        else {
            if (count > most_count) {
                int* most = new int[N];
                most = { 0, };
                most[k] = array[i-1];
                most_count = count;
                k++;
            }
            else if (count == most_count) {
                most[k] = array[i-1];
                k++;
            }
            else {

            }
            count = 0;
        }
        i++;
    }
    if (k >= 2) {
        return most[1];
    }
    else if(k == 1){
        return most[0];
    }
    else {
        if (N < 2) {
            return array[0];
        }
        else {
            return array[1];
        }
    }
}

int main() {
    int N = 0;
    int average = 0;
    int most = 0;
    scanf_s("%d", &N);
    int* array = new int[N];
    int* temp = new int[N];
    for (int i = 0; i < N; i++) {
        scanf_s("%d", &array[i]);
        average += array[i];
    }
    average = average / N;
    printf("%d\n", average);

    mergeSort(array,temp,0,N-1);
    printf("%d\n", array[N / 2]);

    //printf("%d\n", array[0]);
    most = findMostUsed(array, N);
    printf("%d", most);

    printf("%d\n", array[N-1] - array[0]);
    return 0;
}*/
/*1181 단어정렬 (c++ 내장라이브러리인 algorithm, vector 처음 사용해봄) 
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int compare(string a, string b) {
    if (a.length() == b.length()) {
        return a < b;
    }
    return a.length() < b.length();
}
int main() {
    int N = 0;
    cin >> N;
    vector<string> arr;
    for (int i = 0; i < N; i++) {
        string temp;
        cin >> temp;
        if (find(arr.begin(), arr.end(), temp) == arr.end()) {
            arr.push_back(temp);
        }
    }
    sort(arr.begin(), arr.end(), compare);
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << '\n';
    }
    return 0;
}*/
/*10815 숫자카드 (정렬 후 이진탐색)
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int isFind = 0;
    int N = 0;
    int M = 0;
    int temp = 0;
    vector<int> array;
    vector<int> result;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> temp;
        array.push_back(temp);
    }
    sort(array.begin(), array.end());
    
    cin >> M;
    for (int i = 0; i < M; i++) {
        isFind = 0;
        cin >> temp;
        int left = 0;
        int right = N - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (array[mid] == temp) {
                result.push_back(1);
                isFind = 1;
                break;
            }
            else if (array[mid] > temp) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        if (isFind == 0) {
            result.push_back(0);
        }
    }
    for (int i = 0; i < M; i++) {
        cout << result[i] << " ";
    }
    return 0;
}*/
/*10816 숫자카드2 lower_bound, upper_bound
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int isfinded = 0;
    int N = 0, M = 0;
    int temp = 0;
    vector<int> array;
    vector<int> result;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> temp;
        array.push_back(temp);
    }
    sort(array.begin(), array.end());
    
    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> temp;
        result.push_back(upper_bound(array.begin(), array.end(), temp) - lower_bound(array.begin(), array.end(), temp));
    }
    for (int i = 0; i < M; i++) {
        cout << result[i] << " ";
    }

    return 0;
}*/
/*1764 듣보잡 >> 두 배열을 이어붙힌 후 정렬하면 같은것 끼리 붙어있음!
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> array1;
vector<string> result;

int main() {
    int N = 0, M = 0;
    string temp;
    cin >> N;
    cin >> M;

    for (int i = 0; i < N; i++) {
        cin >> temp;
        array1.push_back(temp);
    }
    for (int i = 0; i < M; i++) {
        cin >> temp;
        array1.push_back(temp);
    } 

    sort(array1.begin(), array1.end());
    
    for (int i = 0; i < N + M - 1; i++) {
        if (array1[i] == array1[i + 1]) {
            result.push_back(array1[i]);
        }
    }

    printf("%d", result.size());
    for (int i = 0; i < result.size(); i++) {
        printf("\n%s", result[i].c_str());
    }
    return 0;
}*/