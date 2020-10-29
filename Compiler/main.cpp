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

int main() {
    freopen("main.jj", "r", stdin);

    string s;

    while (getline(cin, s)) {
        if (s.find("print") != string :: npos) {
            string buff = s.substr(6, s.size() - 1);

            cout << values[buff];

        } else {
            string value = s.substr(0, s.find("=") - 1);
            string buf = s.substr(s.find("=") + 2, s.size() - 1);

            while (string :: npos != buf.find("+ ")) {
                buf.erase(buf.find("+ "), 2);
            }

            string s = "";
            int k = 0;

            for (int i = 0; i < buf.size(); i++) {
                if (buf[i] == ' ') {
                    if (('a' <= s[0] && s[0] <= 'z') || ('A' <= s[0] && s[0] <= 'Z')) {
                        k += values[s];
                    } else {
                        k += strToInt(s);
                    }

                    s = "";
                } else {
                    s += buf[i];
                }
            }

            if (('a' <= s[0] && s[0] <= 'z') || ('A' <= s[0] && s[0] <= 'Z')) {
                k += values[s];
            } else {
                k += strToInt(s);
            }

            values[value] = k;
        }
    }

    return 0;
}
