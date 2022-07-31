/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeElements(struct ListNode* head, int val){
    struct ListNode *cur,*prev;
    cur=head;
    prev=NULL;
    while(cur!=NULL)
    {
        if(cur->val==val)
        {
            if(prev==NULL)
                head=cur->next;
            else
                prev->next=cur->next;
        }
        else
            prev=cur;
        cur=cur->next;
    }   
    return head;
}