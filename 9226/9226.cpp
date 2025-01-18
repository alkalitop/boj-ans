#include <bits/stdc++.h>
using namespace std;

bool is_vowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main() {
    string word;
    cin >> word;
    do {
        int i = 0;
        while (i < word.size() && !is_vowel(word[0])) {
            word.append(1, word[0]);
            word.erase(0, 1);
            ++i;
        }
        cout << word << "ay" << endl;
        cin >> word;
    } while (word != "#");
    return 0;
}
