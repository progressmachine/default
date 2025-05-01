#include <iostream>

int main() {
    int x; // declaration
    x = 5; // assignment
    int y = 6;
    int sum = x + y;

    std::cout << x << "\n";
    std::cout << y << "\n";
    std::cout << sum << "\n";

    double price = 25.99;
    std::cout << price << "\n";

    char grade = 'A';
    std::cout << grade << '\n';

    bool student = true;
    bool power_on = true;
    bool for_sale = false;

    // Strings: objects that represent a sequence of text.
    std::string name = "Tom White";
    std::cout << "Hello, " << name << "." << std::endl;

    return 0;
}