#include <iostream>
using namespace std;
void infix(string x){
    string a={};

    for (int i; i <= (x.length()); i++)
    {

        if (x[i] = '(')
        {
            a.append(x[i]);
        }
    }
}
int main(int argc, char const *argv[])
{

    string temp = "(a+b)*b-c";
    cout << temp;
    return 0;
}
