#include <iostream>



int main(){
    std::string inp;
    std::cin >> inp;
    int l = inp.length();

    
    std::string num[l/2  + 1];
    for (int i = 0; i <= l - 1; i = i + 2){
        num[i/2] = inp[i];
    }
    
    //insertion sort
    int i = 1;
    while (i < l/2  + 1 ){
        std::string x = num[i];
        int j = i - 1;
        while ((j >= 0) && (num[j] > x)){
            num[j + 1] = num[j];
            j  = j - 1;
        }
        num[j + 1] = x;
        i++;
    }
    
    std::string out;
    out = num[0];
    for (int k = 1; k <= l/2; k++){
        out += "+" + num[k];
    }
    std::cout << out;
    return 0;
}