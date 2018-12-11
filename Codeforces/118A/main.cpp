#include <iostream>
#include <string>

int main(){
    std::string inp;
    std::cin >> inp;

    int l = inp.length();
    std::string out = "";
    for (int i = 0; i <= l - 1; i++){
        char cur = tolower(inp[i]);
        if ((cur == 'a') || (cur == 'o') || (cur == 'y') || (cur == 'e') || (cur == 'u') || (cur == 'i')){
            int j = 0;
        }
        else{
            out += ".";
            out += cur;
        }
    }
    std::cout << out << std::endl;
    return 0;
}