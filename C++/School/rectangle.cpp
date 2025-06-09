// Include input-output stream library
#include <iostream>

// Include math library (not used here but included in original)
#include <cmath>

// Use standard namespace to avoid prefixing with std::
using namespace std;

// Define a class named Rectangle
class Rectangle {
    int l, b; // Declare private members for length and breadth

public:
    // Default constructor sets length and breadth to 0
    Rectangle() { l = 0; b = 0; }

    // Parameterized constructor to set length and breadth
    Rectangle(int p, int q) { l = p; b = q; }

    // Function to take user input for length and breadth
    void setter() {
        cout << "Enter length and breadth: ";
        cin >> l >> b;
    }

    // Function to calculate area
    int area() { return l * b; }

    // Function to calculate perimeter
    int peri() { return 2 * (l + b); }
};

// Main function
int main() {
    Rectangle a;        // Create a Rectangle object
    a.setter();         // Get length and breadth from user
    cout << "area=" << a.area(); // Print area
    cout << "peri=" << a.peri(); // Print perimeter
}
