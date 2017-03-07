//法1
public class Solution {
public String longestCommonPrefix(String[] strs) {
    if (strs.length == 0) return "";
    String prefix = strs[0];
    for (int i = 1; i < strs.length; i++)
	//indexOf返回 String 对象内第一次出现子字符串的字符位置,，没有返回-1
        while (strs[i].indexOf(prefix) != 0) { //要从头开始一样
            prefix = prefix.substring(0, prefix.length() - 1);  //不一样，公共前缀去掉一个字符
            if (prefix.isEmpty()) return "";
        }        
    return prefix;
}
}

//法2
public class Solution {
public String longestCommonPrefix(String[] strs) {
    if (strs == null || strs.length == 0) return "";
    for (int i = 0; i < strs[0].length() ; i++){
        char c = strs[0].charAt(i);//对第一个字符串的每一个字符
        for (int j = 1; j < strs.length; j ++) { //看看其余字符串的相同位置的字符是不是也是这个
            if (i == strs[j].length() || strs[j].charAt(i) != c)
                return strs[0].substring(0, i);             
        }
    }
    return strs[0];
}
}
//法3
public class Solution {
	public String longestCommonPrefix(String[] strs) {
    		if (strs == null || strs.length == 0) return "";    
        	return longestCommonPrefix(strs, 0 , strs.length - 1);
	}

	private String longestCommonPrefix(String[] strs, int l, int r) {
    		if (l == r) {
        		return strs[l];
    		}
    		else {
        		int mid = (l + r)/2;
        		String lcpLeft =   longestCommonPrefix(strs, l , mid);
        		String lcpRight =  longestCommonPrefix(strs, mid + 1,r);
        		return commonPrefix(lcpLeft, lcpRight);
   		}
	}

	String commonPrefix(String left,String right) {
    		int min = Math.min(left.length(), right.length());       
    		for (int i = 0; i < min; i++) {
        		if ( left.charAt(i) != right.charAt(i) )
            			return left.substring(0, i);
    		}
    		return left.substring(0, min);
	}
}

