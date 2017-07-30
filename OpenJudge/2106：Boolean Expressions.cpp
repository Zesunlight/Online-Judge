#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>

using namespace std;
int factor();
int term();
int expression();
char peekChar();

int main()
{

    int number = 0;
    while (peekChar() != -1) {
        cout << "Expression " << ++number << ": ";
        if (expression() == 1)
            cout << 'V' << endl;
        else
            cout << 'F' << endl;
    }

    return 0;
}

char peekChar()
{
    char c = '\0';
    c = cin.peek();
    while (c == ' ' || c == '\n') {
        cin.get();
        c = cin.peek();
    }
    return c;
}

int expression()
{
    int result = term();
    char c = '\0';
    while (1) {
        c = peekChar();
        if (c == '&') {
            cin.get();
            result = result & term();
        } else if (c == '|') {
            cin.get();
            result = result | term();
        } else
            break;
    }

    return result;
}

int term()
{
    char c = peekChar();
    int result = 0;
    if (c == '!') {
        cin.get();
        result = !term();
    } else
        result = factor();

    return result;
}

int factor()
{
    char c = peekChar();
    int result = 0;
    cin.get();
    if (c == '(') {
        result = expression();
        c = peekChar();
        cin.get();
    } else if (c == 'F')
        result = 0;
    else
        result = 1;

    return result;
}
