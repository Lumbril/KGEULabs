#include <iostream>
#include <vector>
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
    if (s.find("In this chapter") != string :: npos) {
        s.insert(s.find("In this chapter"), "\t");
    }

    if (s.find("The output from") != string :: npos) {
        s.insert(s.find("The output from"), "\n\t");
    }

    if (s.find("If the notation") != string :: npos) {
        s.insert(s.find("If the notation"), "\n\t");
    }

    return s;
}

string numberedList(string s) {
    if (s.find("1.") != string :: npos) {
        s.insert(s.find("1."), "\n\n\t");
    }

    if (s.find("2.") != string :: npos) {
        s.insert(s.find("2."), "\n\t");
    }

    if (s.find("3.") != string :: npos) {
        s.insert(s.find("3."), "\n\t");
        s += "\n";
    }

    return s;
}

int counterLetters(string s) {
    int ans = 0;

    for (int i = 0; i < s.size(); i++) {
        if (('a' <= s[i] && s[i] <= 'z') || ('A' <= s[i] && s[i] <= 'Z')) {
            ans++;
        }
    }

    return ans;
}

int counterNumbers(string s) {
    int ans = 0;

    for (int i = 0; i < s.size(); i++) {
        if ('0' <= s[i] && s[i] <= '9') {
            ans++;
        }
    }

    return ans;
}

int counterWords(string s) {
    vector <string> a;
    string buf = "";

    for (int i = 0; i < s.size(); i++) {
        if (('a' <= s[i] && s[i] <= 'z') || ('A' <= s[i] && s[i] <= 'Z') || ('0' <= s[i] && s[i] <= '9')) {
            buf += s[i];
        } else {
            if (buf != "") {
                a.push_back(buf);
                buf = "";
            }
        }
    }

    a.push_back(buf);

    int ans = 0;
    for (int i = 0; i < a.size(); i++) {
        if (('a' <= a[i][0] && a[i][0] <= 'z') || ('A' <= a[i][0] && a[i][0] <= 'Z')) {
            ans++;
        }
    }

    return ans;
}

string statistic(string s) {
    int countPars = 4;
    int countRows = 6;
    int countWords = counterWords(s);
    int countLetters = counterLetters(s);
    int countNums = counterNumbers(s);
    int countOther = s.size() - countLetters - countNums;
    int sumSymb = countLetters + countNums + countOther;

    return "\n\nКоличество абзацев = " + to_string(countPars) +
        "\nКоличество строк = " + to_string(countRows) +
        "\nКоличество слов = " + to_string(countWords) +
        "\nКоличество символов = " + to_string(sumSymb) +
        "\n\tиз них \tбукв \t\t\t= " + to_string(countLetters) +
        "\n	\t\tцифр \t\t\t= " + to_string(countNums) +
        "\n\t\t	других символов \t= " + to_string(countOther);
}

int main() {
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
