#include <iostream>

int main() {
    int n, totacertos = 0;
    std::cin >> n;
    char gabarito[n], respostas[n] = {};

    for (int i = 0; i < n; i++) {
        std::cin >> gabarito[i];
    }
    for (int i = 0; i < n; i++) {
        std::cin >> respostas[i];
    }
    for (int i = 0; i< n; i++) {
        if (respostas[i] == gabarito[i]) {
            totacertos++;
        }
    }
    std::cout << totacertos << std::endl;
    return 0;
}
