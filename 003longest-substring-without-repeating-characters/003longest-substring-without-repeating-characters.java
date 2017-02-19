public class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length()==0)
          return 0;
        int start=0;
        int end=0;
        int maxLen=0;
        HashMap<Chaacter,Integer> charMap=new HashMap<Character,Integer>();
        while(end<s.length()){
            if(!charMap.containsKey(s.charAt(end))){
                charMap.put(s.charAt(end),end);
                int len=end-start+1;
                maxLen=Math.max(len,maxLen);
            }
            else{
                int val=charMap.get(s.charAt(end));
                for(int i=start;i<val+1;i++)
                   charMap.remove(s.charAt(i));
                start=val+1;
                charMap.put(s.charAt(end),end);
            }
            end++;
        }
        return maxLen;
    }
}
