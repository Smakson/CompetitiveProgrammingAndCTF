#include <iostream>
#include <string>

int main(){
    std::string a,b;
    std::cin >> a >> b;
    for (int i = 0; i <= a.length() - 1; i++){
        a[i] = tolower(a[i]);
    }
    for (int j = 0; j <= b.length() - 1; j++){
        b[j] = tolower(b[j]);
    }
    
    if (a == b){
        std::cout << 0;
    }
    else if (a < b){
        std::cout << -1;
    }
    else if (a > b){
        std::cout << 1;
    }
    return 0;
}