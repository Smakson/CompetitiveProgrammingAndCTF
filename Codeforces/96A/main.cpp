#include <iostream>
#include <string>

int main(){
    std::string seq;
    std::cin >> seq;

    int l = seq.length();
    int count = 1;
    char cur = seq[0];
    for (int i = 1; i <= l - 1; i++){
        if (cur == seq[i]){
            count += 1;
            if (count == 7){
                std::cout << "YES";
                return 0;
            }
        }
        else{
            count = 1;
            cur = seq[i];
        }
    }

    
    std::cout << "NO";

    return 0;
}