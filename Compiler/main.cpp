#include <bits/stdc++.h>
using namespace std;

map<string, int> values;

int strToInt(string str) {
    int ans = 0;

    for (int i = 0; i < str.size(); i++) {
        ans *= 10;
        ans += str[i] - '0';
    }

    return ans;
}

string deleteAllSpace(string str) {
    for (int i = 0; i < str.size(); i++) {
        if (str[i] == ' ') {
            str.erase(i, 1);
        }
    }

    return str;
}

int main() {
    freopen("main.jj", "r", stdin);

    string s;

    while (getline(cin, s)) {
        if (s.find("print") != string :: npos) {
            string buff = s.substr(6, s.size() - 1);

            cout << values[buff];

        } else {
            s = deleteAllSpace(s);

            string value = s.substr(0, s.find("="));
            string buf = s.substr(s.find("=") + 1, s.size() - 1);

            while (string :: npos != buf.find("+")) {
                //buf.erase(buf.find("+"), 1);
                buf[buf.find("+")] = ' ';
            }

            string str = "";
            int k = 0;

            for (int i = 0; i < buf.size(); i++) {
                if (buf[i] == ' ') {
                    if (('a' <= str[0] && str[0] <= 'z') || ('A' <= str[0] && str[0] <= 'Z')) {
                        k += values[str];
                    } else {
                        k += strToInt(str);
                    }

                    str = "";
                } else {
                    str += buf[i];
                }
            }

            if (('a' <= str[0] && str[0] <= 'z') || ('A' <= str[0] && str[0] <= 'Z')) {
                k += values[str];
            } else {
                k += strToInt(str);
            }

            values[value] = k;
        }
    }

    return 0;
}
