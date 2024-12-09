#include <iostream>

int main() {
    int n, p, c, totp = 0;
    std::cin >> n;
    int baloes[n] = {};
    for (int i = 0; i < n; i++) {
        std::cin >> p;
        baloes[i] = p;
    }
    std::cin >> c;
    for (int i = 0; i < n; i++) {
        if (baloes[i] == c) {
            totp -= c;
        } else {
            totp += baloes[i];
        }
    }
    std::cout << totp << std::endl;
    return 0;
}