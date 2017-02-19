/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode re=new ListNode(0);
        ListNode cur=re;
        int flag=0,num1=0,num2=0;
        while(l1!=null||l2!=null){
            num1=l1==null?0:l1.val;
            num2=l2==null?0:l2.val;
            ListNode node=new ListNode((num1+num2+flag)%10);
            flag=(num1+num2+flag)/10;
            cur.next=node;
            cur=node;
            if(l1!=null)
               l1=l1.next;
            if(l2!=null)
               l2=l2.next;
        }
        //最高位进位
        if(flag==1){
            cur.next=new ListNode(1);
            cur=cur.next;
        }
        
        cur.next=null;
        return re.next;
    }
}
