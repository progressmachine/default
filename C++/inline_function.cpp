// Inline functions trade memory for speed.
// The compiler tries to replace the function call with the actual code.

#include <iostream>
using namespace std;

// Normal function
int add_normal(int a, int b) {
    return a + b;
}

// Inline function
inline int add_inline(int a, int b) {
    return a + b;
}

int main() {
    int x = 2, y = 3;

    int result1 = add_normal(x, y);  // Normal function call
    int result2 = add_inline(x, y);  // Inline function call (may be replaced directly)

    cout << "Normal function result: " << result1 << endl;
    cout << "Inline function result: " << result2 << endl;

    return 0;
}


// •	Both functions do the same thing: add two numbers.
// •	But for add_inline, the compiler might replace the call with x + y directly — like a shortcut.
// •	You won’t see a difference in output, but internally, the inline version can be a little faster.

// Why not use inline for big or complex functions?

/*

inline int bigFunction() {
    // Imagine 100 lines of logic here
}

And you call it 1000 times, the compiler might literally paste those 100 lines 1000 times in your program.

🚨 Problems:
	•	Code bloat: Your program gets much larger in memory (slower to load, cache-unfriendly).
	•	Slower compilation: The compiler has to process that same big code many times.
	•	Less efficient optimizations: Ironically, sometimes it makes performance worse.

🧠 Inline is great for small 1–2 line functions like return a + b;.

*/

/*
Why say “may be replaced directly”?

Because:

🛠 inline is only a request, not a command.

C++ gives the compiler the final say. It may choose to:
	•	Inline it (replace the call with code)
	•	Ignore your inline keyword completely

Why?

The compiler tries to optimize overall performance, not just inlining:
	•	It might ignore inline if the function is too big or used in a weird way.
	•	It might inline a normal function if it thinks it’s safe and fast to do so.
*/