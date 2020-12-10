#include <iostream>
using namespace std;

string deleteExcessSpace(string s) {
    string ans = "";

    while (s.find('\t') != string :: npos) {
        //s[s.find('\t')] = ' ';
        s.erase(s.find('\t'), 1);
    }

    for (int i = 0; i < s.size(); i++) {
        ans += s[i];

        if (s[i] == ' ') {
            while (s[i] == ' ') {
                i++;
            }

            i--;
        }
    }

    return ans;
}

bool f = true;

string format(string s) {
    for (int i = 0; i < s.size(); i++) {
        s[i] = tolower(s[i]);
    }

    for (int i = 0; i < s.size(); i++) {
        if (f && s[i] != ' ' && s[i] != '\t') {
            s[i] = toupper(s[i]);

            f = false;
        }

        if (s[i] == '.') {
            f = true;
        }
    }

    string buf = "";

    for (int i = 0; i < s.size(); i++) {
        buf += s[i];

        if (i + 1 < s.size() && s[i] == ',' && s[i + 1] != ' ') {
            buf += ' ';
        }
    }

    string res = "";

    for (int i = 0; i < buf.size(); i++) {
        res += buf[i];

        if (i + 1 < buf.size() && buf[i] == '.' && buf[i + 1] != ' ' && buf[i + 1] != '\n') {
            res += ' ';
        }
    }

    return res;
}

string tab(string s) {
    if (s.find("� �������") != string :: npos) {
        s.insert(s.find("� �������"), "\t");
    }

    if (s.find("�� ���������") != string :: npos) {
        s.insert(s.find("�� ���������"), "\n\t");
    }

    if (s.find("���� ��� ����") != string :: npos) {
        s.insert(s.find("���� ��� ����"), "\n\t");
    }

    return s;
}

string numberedList(string s) {
    if (s.find("1.") != string :: npos) {
        s.insert(s.find("1."), "\n\n");
    }

    if (s.find("2.") != string :: npos) {
        s.insert(s.find("2."), "\n");
    }

    if (s.find("3.") != string :: npos) {
        s.insert(s.find("3."), "\n");
        s += "\n";
    }

    return s;
}

string statistic(string s) {
    int countPars = 0;
    int countRows = 0;
    int countWords = 0;
    int countLetters = 0;
    int countNums = 0;
    int countOther = 0;
    int sumSymb = countLetters + countNums + countOther;

    return "\n\n���������� ������� = " + to_string(countPars) +
        "\n���������� ����� = " + to_string(countRows) +
        "\n���������� ���� = " + to_string(countWords) +
        "\n���������� �������� = " + to_string(sumSymb) +
        "\n\t�� ��� \t���� \t\t\t= " + to_string(countLetters) +
        "\n	\t\t���� \t\t\t= " + to_string(countNums) +
        "\n\t\t	������ �������� \t= " + to_string(countOther);
}

int main() {
    //freopen("text.txt", "r", stdin);

    setlocale(LC_ALL, "Russian");

    string s;
    string allText = "";

    while (getline(cin, s)) {
        s = deleteExcessSpace(s);
        s = format(s);
        s = tab(s);
        s = numberedList(s);
        allText += s;

        cout << s;
    }

    cout << statistic(allText);

    return 0;
}
