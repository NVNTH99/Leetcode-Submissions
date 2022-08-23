/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverse(struct ListNode *x,struct ListNode *y,struct ListNode *z)
{
    y->next = x;
    if(z==NULL)
        return y;
    return reverse(y,z,z->next);
}
struct ListNode* reverseList(struct ListNode* head){
    if(head==NULL)
        return head;
    return reverse(NULL,head,head->next);
}