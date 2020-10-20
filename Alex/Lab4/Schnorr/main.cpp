#include <bits/stdc++.h>
using namespace std;

long long primeNumbers[99]{
    3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541
};

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

long long searchG(long long q, long long p) {
    long long ans = 2;

    while (powMod(ans, q, p) != 1) {
        ans++;
    }

    return ans;
}

long long modinv(long long a, long long m) {
    long long x;
    long long y;
    long long g = gcd(a, m, x, y);

    return (x % m + m) % m;
}

int main() {
    srand(time(0));
    setlocale(LC_ALL, "Russian");

    long long p = primeNumbers[rand() % 99];
    vector<long long> div;

    for (int i = 2; i * i <= p - 1; i++) {
        if ((p - 1) % i == 0) {
            div.push_back((p - 1) / i);
        }
    }

    long long q = div[rand() % div.size()];
    long long g = searchG(q, p);
    long long w = rand() % q;
    long long y = powMod(modinv(g, p), w, p);

    cout << "Public key: (" << p << ", " << q << ", " << g << ", " << y << ")\n";
    cout << "Secret key: (" << w << ")\n\n";
    cout << "***Checking***\n";

    long long r = rand() % q;
    long long x = powMod(g, r, p);
    long long e = rand() % (4095);
    long long s = (r + w * e) % q;

    cout << x << " " << (powMod(g, s, p) * powMod(y, e, p)) % p << "\n";

    if (x == (powMod(g, s, p) * powMod(y, e, p)) % p)
        cout << "OK";

    return 0;
}
