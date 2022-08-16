/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    if(head==NULL)
        return head;
    struct ListNode *x = head;
    struct ListNode *y = x->next;
    while(y!=NULL)
    {
        if(x->val == y->val)
        {
            x->next = y->next;
            y=y->next;
            continue;
        }
        x=x->next;
        y=y->next;
    }
    return head;
}