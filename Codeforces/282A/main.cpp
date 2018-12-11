#include <iostream>
#include <string>

int main(){
    int n;
    std::cin >> n;
    int x = 0;
    
    for (int i = 0; i <= n - 1; i++){
        std::string com;
        std::cin >> com;
        if ((com == "X++") || (com == "++X")){
            x += 1;
        }

        if ((com == "X--") || (com == "--X")){
            x -= 1;
        }
    }
    

    std::cout << x;
    return 0;
}