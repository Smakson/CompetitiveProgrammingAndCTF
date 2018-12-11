#include <iostream>

int main(){
    int n,k;
    std::cin >> n >> k;
    int scores[n];
    for (int i = 0; i <= n - 1; i++){
        std::cin >> scores[i];
    }
    
    int min = scores[k - 1];
    int count = 0;
    int ind = 0;
    while ((scores[ind] >= min) && (scores[ind] > 0) && (ind < n)){
        count++;
        ind++;
    }
    std::cout << count;
    return 0;
}