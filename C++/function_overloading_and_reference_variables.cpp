#include <iostream>
using namespace std;

// Function overloading: same name, different parameters

// Version 1: takes two integers by value
int add(int a, int b) {
    return a + b;
}

// Version 2: takes two doubles by value
double add(double a, double b) {
    return a + b;
}

void reference_example(int &a, int &b) { // this won't be used in function overloading by calling it add cause int parameters are still int,int the & doesn't change anything
    a += 1;  // Modify the original variables
    b += 1;
}

int main() {
    int x = 5, y = 10;
    double p = 2.5, q = 3.5;

    // Calls version 1
    cout << "add(int, int): " << add(2, 3) << endl;

    // Calls version 2
    cout << "add(double, double): " << add(p, q) << endl;

    cout << "x before add: " << x << endl;
    cout << "y before add: " << y << endl;

    reference_example(x, y);

    // Check if original variables changed
    cout << "x after add: " << x << endl;
    cout << "y after add: " << y << endl;

    return 0;
}