#include <iostream>
#include <string>

int main() {
    std::string a, b;
    std::cin >> a >> b;

    if (a == "direita" && b == "esquerda") {
        std::cout << "Achou" << std::endl;
    } else if (a == "esquerda" && b == "esquerda") {
        std::cout << "Morreu" << std::endl;
    } else {
        std::cout << "Tente novamente" << std::endl;
    }
    return 0;
}