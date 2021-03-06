/*
 * Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

 */

#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>

using namespace std;

class Solution {
public:
    void reverseWords(string &s) {
        string res = "";
        int left = -1, right = -1;
        for (int i = s.length() - 1; i >= 0; --i) {
            if (s[i] == ' ') {
                if (left < 0 && right > 0) {
                    left = i + 1;
                    if (res.length() > 0) {
                        res += ' ';
                    }
                    // caution!!! 2nd param is length
                    res += s.substr(left, right - left);
                    right = -1;
                }
            } else {
                if (right < 0) {
                    right = i + 1;
                    left = -1;
                }
            }
        }

        // caution!!!
        if (right > 0) {
            if (res.length() > 0) {
                res += ' ';
            }
            res += s.substr(0, right);
        }
        s = res;
    }
};


int main() {
    string s = "the   sky is blue";
    Solution solution;
    solution.reverseWords(s);
    cout << s << endl;

    s = "hello";
    solution.reverseWords(s);
    cout << s << endl;

    s = " ";
    solution.reverseWords(s);
    cout << s << endl;

    s = " 1";
    solution.reverseWords(s);
    cout << s << endl;

    s = " 1 ";
    solution.reverseWords(s);
    cout << s << endl;

    s = "hello world!";
    solution.reverseWords(s);
    cout << s << endl;

}