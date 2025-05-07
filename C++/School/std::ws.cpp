#include <iostream>
#include <string>

// Function overload 1: adds two integers
int add(int a, int b) {
    return a + b;
}

// Function overload 2: concatenates two strings
std::string add(const std::string& a, const std::string& b) {
    return a + " " + b;
}

int main() {
    int x, y;
    std::string first, last;

    // Input two integers
    std::cout << "Enter two integers: ";
    std::cin >> x >> y;

    // Clear newline before getline
    std::cin.ignore(); // OR use std::getline(std::cin >> std::ws, ...)

    // Input two strings (first and last name)
    std::cout << "Enter your first name: ";
    std::getline(std::cin >> std::ws, first);

    std::cout << "Enter your last name: ";
    std::getline(std::cin >> std::ws, last);

    // Call both overloaded functions
    int sum = add(x, y);
    std::string fullName = add(first, last);

    // Output results
    std::cout << "Sum: " << sum << std::endl;
    std::cout << "Full name: " << fullName << std::endl;

    return 0;
}