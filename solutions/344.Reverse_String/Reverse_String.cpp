# include <iostream>
# include <string>

using namespace std;

class Solution {
public:
    // 雙指針
    string reverseString(string s)
    {
        int i = 0;
        int j = s.size()-1;
        while (i < j)
        {
            char tmp = s[j];
            s[j] = s[i];
            s[i] = tmp;
            i++;
            j--;
        }
        return s;
    }

    /*
    {
        for (int L=0, R=s.size()-1; L<R; L++, R--){
            char tmp = s[R];
            s[R] = s[L];
            s[L] = tmp;
        }
        return s;
    }
    */

};
