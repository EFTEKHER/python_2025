#include <iostream>
using namespace std;

class Counter {
    static int count; // declaration (shared by all objects)
public:
    Counter() {
        count++;
        cout << "Constructor called. Count = " << count << endl;
    }
    ~Counter() {
        cout << "Destructor called. Count = " << count << endl;
        count--;
    }
};

// definition of static member (outside the class)
int Counter::count = 0;

int main() {
    Counter a, b;
    {
        Counter c;
    }
    Counter d;
    return 0;
}
