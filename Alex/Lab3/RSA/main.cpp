#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b, long long &x, long long &y) {
	if (a == 0) {
		x = 0;
		y = 1;

		return b;
	}

	long long x1, y1;
	long long d = gcd(b % a, a, x1, y1);

	x = y1 - (b / a) * x1;
	y = x1;

	return d;
}

long long primeNumbers[99]{
    3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541
};

long long p, q;
long long e = 3;
long long n;
long long funcE;
long long g;
long long d;

string message = "";
vector <long long> cryptoText;

long long powMod(long long a, long long n, long long m) {
    long long ans = 1;

    while (n) {
        if (n & 1) {
            ans *= a;
            ans %= m;
            n--;
        } else {
            a *= a;
            a %= m;
            n >>= 1;
        }
    }

    return ans;
}

long long crypt(long long a) {
    return powMod(a, e, n);
}

long long decrypt(long long a) {
    return powMod(a, d, n);
}

int main() {
    srand(time(0));
    setlocale(LC_ALL, "Russian");

    do {
        p = primeNumbers[rand() % 99];
        q = primeNumbers[rand() % 99];
        n = p * q;
        funcE = (p - 1) * (q - 1);

        long long m = funcE;

        long long x, y;
        g = gcd(e, m, x, y);
        d = (x % m + m) % m;
    } while (d == 1);

    cout << "Открытый ключ: " << e << ":" << n << "\n";
    cout << "Закрытый ключ: " << d << ":" << n << "\n";

    cout << "Введите сообщение: ";

    string text;

    cin >> text;

    for (int i = 0; i < text.size(); i++) {
        cryptoText.push_back(crypt((long long)text[i]));
    }

    cout << "Зашифрованный текст: ";

    for (int i = 0; i < cryptoText.size(); i++) {
        cout << cryptoText[i] << " ";
    }

    cout << "\n";

    cout << "Расшифрованный текст: ";

    for (int i = 0; i < cryptoText.size(); i++) {
        cout << (char)decrypt(cryptoText[i]);
    }

    return 0;
}
