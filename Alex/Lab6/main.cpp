#include <bits/stdc++.h>
using namespace std;

const double EPS = 1e-9;

vector<vector <double>> A;  //первоначальная матрица, превратиться в обратную матрицу
vector<vector <double>> B;  //копия первой матрицы, для нахождения определителя матрицы А
vector<vector <double>> C;  //результат умножения матриц, должна быть единичной
vector<vector <double>> AT;  //матрица алгеброических дополнений
vector<vector <double>> M;  //матрица миноров

//Заполнение по 3ему варианту
void inputArray() {
    int k = -1;
    int val = 1;

    for (int i = 0; i < A.size(); i++) {
        k *= -1;

        if (k > 0) {
            for (int j = 0; j < A[i].size(); j += k){
                A[j][i] = val++;
            }
        } else {
            for (int j = A[i].size() - 1; j > -1; j += k){
                A[j][i] = val++;
            }
        }
    }
}

void copyArray() {
    for (int i = 0; i < A.size(); i++) {
        for (int j = 0; j < A[i].size(); j++) {
            B[i][j] = A[i][j];
        }
    }
}

//Транспонирование матрицы AT
void T() {
    vector<vector <double>> buff;

    buff.resize(AT.size());

    for (int i = 0; i < AT.size(); i++) {
        buff[i].resize(AT[i].size());
    }

    for (int i = 0; i < AT.size(); i++) {
        for (int j = 0; j < AT[i].size(); j++) {
            buff[j][i] = AT[i][j];
        }
    }

    for (int i = 0; i < AT.size(); i++) {
        for (int j = 0; j < AT[i].size(); j++) {
            AT[i][j] = buff[i][j];
        }
    }
}

//Нахождение определителя методом Гаусса
double searchDet() {
    double det = 1;

    for (int i = 0; i < B.size(); i++) {
        int k = i;

        for (int j = i + 1; j < B[i].size(); j++) {
            if (abs(B[j][i]) > abs(B[k][i])) {
                k == j;
            }
        }

        if (abs(B[k][i]) < EPS) {
		    det = 0;
		    break;
	    }

	    swap(B[i], B[k]);

	    if (i != k) {
	        det = -det;
	    }

	    det *= B[i][i];

	    for (int j = i + 1; j < B[i].size(); j++) {
	        B[i][j] /= B[i][i];
	    }

	    for (int j = 0; j < B[i].size(); j++) {
	        if (j != i && abs(B[j][i]) > EPS) {
	            for (int k = i + 1; k < B[i].size(); k++) {
	                B[j][k] -= B[i][k] * B[j][i];
	            }
	        }
	    }
    }

    return det;
}

//Умножение матриц
void multMatrix() {
    for (int i = 0; i < AT.size(); i++) {
        for (int j = 0; j < AT[i].size(); j++) {
            double sum = 0;

            for (int k = 0; k < AT.size(); k++) {
                sum += A[i][k] * AT[k][j];
            }


            C[i][j] = sum > EPS ? sum : 0;
        }
    }
}

void outputArray() {
    for (int i = 0; i < A.size(); i++) {
        for (int j = 0; j < A[i].size(); j++) {
            cout << A[i][j] << " ";
        }

        cout << '\n';
    }
}

//Создание минора
void createMinor(int a, int b) {
    M.resize(A.size() - 1);

    for (int i = 0; i < M.size(); i++) {
        M[i].resize(0);
    }

    int k = 0;

    for (int i = 0; i < A.size(); i++) {
        if (a != i) {
            for (int j = 0; j < A[i].size(); j++) {
                if (b != j) {
                    M[k].push_back(A[i][j]);
                }
            }

            k++;
        }
    }
}

//нахождение определителя минора
double minorDet() {
    double det = 1;

    for (int i = 0; i < M.size(); i++) {
        int k = i;

        for (int j = i + 1; j < M[i].size(); j++) {
            if (abs(M[j][i]) > abs(M[k][i])) {
                k == j;
            }
        }

        if (abs(M[k][i]) < EPS) {
		    det = 0;
		    break;
	    }

	    swap(M[i], M[k]);

	    if (i != k) {
	        det = -det;
	    }

	    det *= M[i][i];

	    for (int j = i + 1; j < M[i].size(); j++) {
	        M[i][j] /= M[i][i];
	    }

	    for (int j = 0; j < M[i].size(); j++) {
	        if (j != i && abs(M[j][i]) > EPS) {
	            for (int k = i + 1; k < M[i].size(); k++) {
	                M[j][k] -= M[i][k] * M[j][i];
	            }
	        }
	    }
    }

    return det;
}

//Создание матрицы алгеброических дополнений
void craeteAT() {
    for (int i = 0; i < A.size(); i++) {
        for (int j = 0; j < A[i].size(); j++) {
            createMinor(i, j);
            AT[i][j] = pow(-1, i + j) * minorDet();
        }
    }
}

int main() {
    setlocale(LC_ALL, "Russian");

    int n;

    cin >> n;

    A.resize(n);
    B.resize(n);
    C.resize(n);
    AT.resize(n);

    for (int i = 0; i < A.size(); i++) {
        A[i].resize(n);
        B[i].resize(n);
        C[i].resize(n);
        AT[i].resize(n);
    }

    inputArray();

    cout << '\n';

    outputArray();

    cout << '\n';

    copyArray();

    double det = searchDet();

    if (det) {
        craeteAT();

        T();

        for (int i = 0; i < AT.size(); i++) {
            for (int j = 0; j < AT[i].size(); j++) {
                AT[i][j] /= det;
            }
        }

        multMatrix();

        for (int i = 0; i < C.size(); i++) {
            for (int j = 0; j < C[i].size(); j++) {
                cout << C[i][j] << " ";
            }

            cout << "\n";
        }
    } else {
        cout << "Obratnoi matrici net!!!\n";
    }

    return 0;
}
