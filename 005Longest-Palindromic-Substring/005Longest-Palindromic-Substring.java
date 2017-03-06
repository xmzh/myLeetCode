public class Solution {
    public String longestPalindrome(String s) {
    int start = 0, end = 0;
    for (int i = 0; i < s.length(); i++) {
        int len1 = expandAroundCenter(s, i, i); //以单个字符为中心开始扩展
        int len2 = expandAroundCenter(s, i, i + 1); //以相邻两个字符为中心开始扩展
        int len = Math.max(len1, len2);
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    return s.substring(start, end + 1);
}

//返回回文串的长度
private int expandAroundCenter(String s, int left, int right) {
    int L = left, R = right;
    while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
        L--; //上面检查到是就扩展了
        R++;
    }
    return R - L - 1;
}

}
