#include <iostream>

int main(){
    int count = 0;
    int n;
    std::cin >> n;
    for (int i = 0; i <= n - 1; i++){
        int o1, o2, o3;
        std::cin >> o1 >> o2 >> o3;
        int s = o1 + o2 + o3;
        if (s >= 2){
            count += 1;
        }
    }
    std::cout << count;
    
    return 0;
}