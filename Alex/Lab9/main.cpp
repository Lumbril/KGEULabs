#include <iostream>
#include <string>
using namespace std;

const int n = 10;

string a[n][4] = {
    "Васильев", "Алексей", "ПИ-2-20", "3,7",
    "Соловьев", "Данил", "ПИ-1-20", "4,5",
    "Петров", "Иван", "ПИ-1-20", "4,0",
    "Иванов", "Дмитрий", "ТРП-1-20", "3,5",
    "Иванов", "Арсен", "ТРП-1-20", "3,3",
    "Краснов", "Дмитрий", "АУБ-1-20", "3,6",
    "Васильева", "Мария", "ТРП-2-20", "4,0",
    "Тарасов", "Матвей", "ТРП-1-20", "3,3",
    "Абдуллин", "Артур", "АУБ-1-20", "3,0",
    "Макаренко", "Арсений", "АУБ-2-20", "4,1"
};

string copyArr[n][4] = {
    "Васильев", "Алексей", "ПИ-2-20", "3,7",
    "Соловьев", "Данил", "ПИ-1-20", "4,5",
    "Петров", "Иван", "ПИ-1-20", "4,0",
    "Иванов", "Дмитрий", "ТРП-1-20", "3,5",
    "Иванов", "Арсен", "ТРП-1-20", "3,3",
    "Краснов", "Дмитрий", "АУБ-1-20", "3,6",
    "Васильева", "Мария", "ТРП-2-20", "4,0",
    "Тарасов", "Матвей", "ТРП-1-20", "3,3",
    "Абдуллин", "Артур", "АУБ-1-20", "3,0",
    "Макаренко", "Арсений", "АУБ-2-20", "4,1"
};

void changeSep() {
    for (int i = 0; i < 10; i++) {
        a[i][3][1] = '.';
    }
}

bool check(string a[], string x[]) {
    if (a[2] > x[2]) {
        return 1;
    } else if (a[2] == x[2]) {
        if (a[0] > x[0]) {
            return 1;
        } else if (a[0] == x[0]) {
            if (a[1] > x[1]) {
                return 1;
            } else if (a[1] == x[1]) {
                if (a[3] > x[3]) {
                    return 1;
                }
            }
        }
    }

    return 0;
}

void selectionSort() {
    changeSep();

    cout << "***Сортировка выбором***\n";

    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;

        for (int j = i + 1; j < n; j++) {
            if (a[j][2] < a[minIndex][2]) {
                minIndex = j;
            } else if (a[j][2] == a[minIndex][2]) {
                if (a[j][0] < a[minIndex][0]) {
                    minIndex = j;
                } else if (a[j][0] == a[minIndex][0]) {
                    if (a[j][1] < a[minIndex][1]) {
                        minIndex = j;
                    } else if (a[j][1] == a[minIndex][1]) {
                        if (stod(a[j][3]) < stod(a[minIndex][3])) {
                            minIndex = j;
                        }
                    }
                }
            }
        }

        if (minIndex != i) {
            swap(a[minIndex], a[i]);
        }
    }
}

void insertionSort() {
    changeSep();

    cout << "***Сортировка вставкой***\n";

    for (int i = 0; i < n; i++) {
        string x[4];

        for (int j = 0; j < 4; j++) {
            x[j] = a[i][j];
        }

        int j;

        for (j = i - 1; j >= 0 && check(a[j], x); j--) {
            for (int k = 0; k < 4; k++) {
                a[j + 1][k] = a[j][k];
            }
        }

        for (int k = 0; k < 4; k++) {
            a[j + 1][k] = x[k];
        }
    }
}

void bubleSort() {
    changeSep();

    cout << "***Сортировка пузырьком***\n";

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (check(a[j], a[j + 1])) {
                swap(a[j], a[j + 1]);
            }
        }
    }
}

void printArray() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 4; j++) {
            cout << a[i][j] << " ";
        }

        cout << '\n';
    }

    cout << '\n';
}

void resetArray() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 4; j++) {
            a[i][j] = copyArr[i][j];
        }
    }
}

int main() {
    setlocale(LC_ALL, "russian");

    selectionSort();
    printArray();

    resetArray();
    insertionSort();
    printArray();

    resetArray();
    bubleSort();
    printArray();

    return 0;
}
