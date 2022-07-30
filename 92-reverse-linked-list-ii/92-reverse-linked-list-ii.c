/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverse(struct ListNode *b,struct ListNode *right)
{
    struct ListNode *a=right->next;
    struct ListNode *c=b->next;
    while(a!=right)
    {
        b->next=a;
        a=b;
        b=c;
        if(c!=NULL)
            c=c->next;
    }
    return a;
}

struct ListNode* reverseBetween(struct ListNode* head, int left, int right)
{
    if(left==right)
        return head;
    struct ListNode *x,*prev;
    x=head;
    prev=NULL;
    int i=1;
    while(i!=left)
    {
        prev=x;
        x=x->next;
        i++;
    }
    while(i!=right)
    {
        x=x->next;
        i++;
    }
    if(prev!=NULL)
        prev->next = reverse(prev->next,x);
    else
        head = reverse(head,x);
    return head;
}