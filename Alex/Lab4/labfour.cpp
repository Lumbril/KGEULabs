#include <bits/stdc++.h>
using namespace std;

/*
0-9 - Рисует соответсвующие цифры
A - Рисует треугольник
# - Рисует квадрат/прямоугольник
+,-,*,/ - Рисует соответсвующие символы
*/

void draw(char type, int width, int height, char symb) {
	double exp = 0.3;
    double k = (double)height / (double) width;
    
    vector<vector<char>> canvas(height);

    for (int i = 0; i < height; i++) {
        canvas[i].resize(width);
    }
    
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
        	canvas[i][j] = ' ';
        }
    }
    
    switch (type) {
        case '0':
        	for (int i = 0; i < canvas.size(); i++) {
        		canvas[i][0] = symb;
        		canvas[i][canvas[0].size() / 2] = symb;
        	}
        	
        	for (int i = 0; i < canvas[0].size() / 2; i++) {
        		canvas[0][i] = symb;
        		canvas[canvas.size() - 1][i] = symb;
        	}
        
            break;
        case '1':
        	for (int i = 0; i < canvas.size(); i++) {
        		canvas[i][canvas[0].size() / 2] = symb;
        	}
        
            break;
        case '2':
        	for (int i = 0; i < canvas[0].size() / 2; i++) {
        		canvas[0][i] = symb;
        		canvas[canvas.size() - 1][i] = symb;
        		canvas[canvas.size() / 2][i] = symb;
        	}
        	
        	for (int i = 0; i < canvas.size() / 2; i++) {
        		canvas[i][canvas[0].size() / 2 - 1] = symb;
        		canvas[i + canvas.size() / 2][0] = symb;
        	}
        
            break;
        case '3':
        	for (int i = 0; i < canvas[0].size() / 2; i++) {
        		canvas[0][i] = symb;
        		canvas[canvas.size() - 1][i] = symb;
        		canvas[canvas.size() / 2][i] = symb;
        	}
        	
        	for (int i = 0; i < canvas.size(); i++) {
        		canvas[i][canvas[0].size() / 2] = symb;
        	}
        
            break;
        case '4':
        	for (int i = 0; i < canvas.size(); i++) {
        		canvas[i][canvas[0].size() / 2] = symb;
        	}
        	
        	for (int i = 0; i < canvas[0].size() / 2; i++) {
        		canvas[canvas.size() / 2][i] = symb;
        	}
        	
        	for (int i = 0; i < canvas.size() / 2; i++) {
        		canvas[i][0] = symb;
        	}
        
            break;
        case '5':
        	for (int i = 0; i < canvas[0].size() / 2; i++) {
        		canvas[0][i] = symb;
        		canvas[canvas.size() - 1][i] = symb;
        		canvas[canvas.size() / 2][i] = symb;
        	}
        	
        	for (int i = 0; i < canvas.size() / 2; i++) {
        		canvas[i][0] = symb;
        		canvas[i + canvas.size() / 2][canvas[0].size() / 2 - 1] = symb;
        	}
        
            break;
        case '6':
        	for (int i = 0; i < canvas[0].size() / 2; i++) {
        		canvas[0][i] = symb;
        		canvas[canvas.size() - 1][i] = symb;
        		canvas[canvas.size() / 2][i] = symb;
        	}
        	
        	for (int i = 0; i < canvas.size(); i++) {
        		canvas[i][0] = symb;
        	}
        	
        	for (int i = canvas.size() / 2; i < canvas.size(); i++) {
        		canvas[i][canvas[0].size() / 2] = symb;
        	}
        	
            break;
        case '7':
        	for (int i = 0; i < canvas.size(); i++) {
        		canvas[i][canvas[0].size() / 2] = symb;
        	}
        	
        	for (int i = 0; i < canvas[0].size() / 2; i++) {
        		canvas[0][i] = symb;
        	}
        	
            break;
        case '8':
        	for (int i = 0; i < canvas[0].size() / 2; i++) {
        		canvas[0][i] = symb;
        		canvas[canvas.size() - 1][i] = symb;
        		canvas[canvas.size() / 2][i] = symb;
        	}
        	
        	for (int i = 0; i < canvas.size(); i++) {
        		canvas[i][0] = symb;
        		canvas[i][canvas[0].size() / 2] = symb;
        	}
        
            break;
        case '9':
        	for (int i = 0; i < canvas[0].size() / 2; i++) {
        		canvas[0][i] = symb;
        		canvas[canvas.size() - 1][i] = symb;
        		canvas[canvas.size() / 2][i] = symb;
        	}
        	
        	for (int i = 0; i < canvas.size(); i++) {
        		canvas[i][canvas[0].size() / 2] = symb;
        	}
        	
        	for (int i = 0; i < canvas.size() / 2; i++) {
        		canvas[i][0] = symb;
        	}
        
            break;
        case 'A':
        	for (int i = 0; i < min(height, width); i++) {
        		canvas[i][i] = symb;
        	}
        	
        	for (int i = 0; i < min(height, width); i++) {
        		canvas[i][0] = symb;
        		canvas[min(height, width) - 1][i] = symb;
        	}
        
            break;
        case '#':
            for (int i = 0; i < canvas.size(); i++) {
                canvas[i][0] = symb;
                canvas[i][canvas[0].size() - 1] = symb;
            }

            for (int i = 0; i < canvas[0].size(); i++) {
                canvas[0][i] = symb;
                canvas[canvas.size() - 1][i] = symb;
            }

            break;
        case '+':
            for (int i = 0; i < canvas.size(); i++) {
                canvas[i][canvas[0].size() / 2] = symb;
            }

            for (int i = 0; i < canvas[0].size(); i++) {
                canvas[canvas.size() / 2][i] = symb;
            }

            break;
        case '-':
            for (int i = 0; i < canvas[0].size(); i++) {
                canvas[canvas.size() / 2][i] = symb;
            }

            break;
        case '*':
        	for (int i = 0; i < canvas.size(); i++) {
				for (int j = 0; j < canvas[i].size(); j++) {
					if (abs(k * j - (height - i)) <= exp) {
						canvas[i][j] = symb;
					}
				}
			}
			
			for (int i = 0; i < canvas.size(); i++) {
				for (int j = 0; j < canvas[i].size(); j++) {
					if (abs(k * j - i) <= exp) {
						canvas[i][j] = symb;
					}
				}
			}
        
            break;
        case '/':
			for (int i = 0; i < canvas.size(); i++) {
				for (int j = 0; j < canvas[i].size(); j++) {
					if (abs(k * j - (height - i)) <= exp) {
						canvas[i][j] = symb;
					}
				}
			}

            break;
        default:
            break;
    }

    for (int i = 0; i < canvas.size(); i++) {
        for (int j = 0; j < canvas[i].size(); j++) {
            cout << canvas[i][j];
        }

        cout << '\n';
    }
}

int main() {
    setlocale(LC_ALL, "Russian");
    
    char type, symb;
    int width, height;

    cout << "Введите тип рисунка: ";
    cin >> type;
    cout << "Введите ширину: ";
    cin >> width;
    cout << "Введите высоту: ";
    cin >> height;
    cout << "Введите символ рисования: ";
    cin >> symb;

    draw(type, width, height, symb);

    return 0;
}
