#include <iostream>
using namespace std;

// Define an inline function to add two numbers
inline int add(int a, int b) {
    return a + b;
}

// Define an inline function to find the square of a number
inline int square(int x) {
    return x * x;
}

int main() {
    int x = 5, y = 10;

    // Using the inline add function
    cout << "Sum of " << x << " and " << y << " is: " << add(x, y) << endl;

    // Using the inline square function
    cout << "Square of " << x << " is: " << square(x) << endl;

    return 0;
}