#include <iostream>
#include <vector>

int main() {
    int c, x = 0;
    std::cin >> c;
    std::vector<char> estradas(c);

    for (int i = 0; i < c; i++) {
        std::cin >> estradas[i];
        switch (estradas[i]) {
            case 'P':
                x += 2;
                break;
            case 'C':
                x += 2;
                break;
            case 'A':
                x += 1;
                break;
            default:
                x += 0;
                break;
        }
    }
    std::cout << x << std::endl;
    return 0;
}